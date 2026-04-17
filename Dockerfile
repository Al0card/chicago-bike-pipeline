FROM python:3.13
WORKDIR /usr/local/pipeline

# Install applicaiton dependencies

COPY pyproject.toml uv.lock ./
RUN pip install uv

RUN uv sync --frozen --no-install-project --no-dev

COPY scripts/ scripts/



CMD ["uv", "run", "scripts/process_all.py"]