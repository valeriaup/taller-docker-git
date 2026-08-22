
FROM python:3.11-slim AS build

WORKDIR /app

COPY src/requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

COPY src/ .


FROM python:3.11-slim AS production

WORKDIR /app

COPY --from=build /root/.local /root/.local
COPY --from=build /app .

ENV PATH=/root/.local/bin:$PATH

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]