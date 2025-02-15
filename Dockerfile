FROM python:3.13-slim

# 防止 Python 生成 .pyc 文件
ENV PYTHONDONTWRITEBYTECODE=1
# 确保 Python 输出直接显示在终端中
ENV PYTHONUNBUFFERED=1

# 安装基本工具
RUN apt-get update && apt-get install -y \
    git \
    curl \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# 安装 Python 工具
RUN pip install --no-cache-dir \
    black \
    pylint \
    pytest \
    ipykernel

# 创建非 root 用户
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME

# 设置工作目录
WORKDIR /workspace

# 切换到非 root 用户
USER $USERNAME