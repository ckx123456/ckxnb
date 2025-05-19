import subprocess
import os
import argparse

def convert_to_h264(input_file, output_file=None, crf=23, preset='medium', log_level='info'):
    """
    使用 FFmpeg 将视频转换为 H.264 编码
    
    参数:
        input_file: 输入视频文件路径
        output_file: 输出视频文件路径，默认为 None（自动生成）
        crf: 视频质量参数，范围 0-51，默认 23（越小质量越高）
        preset: 编码速度预设，默认 'medium'
        log_level: FFmpeg 日志级别，默认 'info'
    """
    # 检查输入文件是否存在
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"输入文件不存在: {input_file}")
    
    # 自动生成输出文件名（如果未指定）
    if not output_file:
        base_name, _ = os.path.splitext(input_file)
        output_file = f"{base_name}_h264.mp4"
    
    # 构建 FFmpeg 命令
    cmd = [
        'ffmpeg',
        '-i', input_file,
        '-c:v', 'libx264',      # 使用 H.264 视频编码
        '-crf', str(crf),       # 设置视频质量
        '-preset', preset,      # 设置编码预设
        '-c:a', 'aac',          # 使用 AAC 音频编码
        '-strict', 'experimental',  # AAC 编码需要
        '-loglevel', log_level, # 设置日志级别
        '-y',                   # 覆盖已存在的输出文件
        output_file
    ]
    
    try:
        # 执行 FFmpeg 命令
        subprocess.run(cmd, check=True)
        print(f"成功将视频转换为 H.264 编码: {output_file}")
        return output_file
    except subprocess.CalledProcessError as e:
        print(f"转换失败: {e}")
        return None
    except Exception as e:
        print(f"发生错误: {e}")
        return None

if __name__ == "__main__":
    # 设置输入和输出路径
    input_file ="images\\japan.mp4"  
    output_file ="images\\japan_h264.mp4"  
    convert_to_h264(input_file, output_file)    
