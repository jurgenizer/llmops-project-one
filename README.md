Project One from the Udemy course [LLMOps Masterclass 2024 - Generative AI - MLOps - AIOps](https://www.udemy.com/course/llmops-masterclass-generative-ai-mlops-aiops/?couponCode=ST20MT50724)

## Install and Run
```
pip install "fastapi[all]"

uvicorn main:app --reload
```

## Test with Postman

http://127.0.0.1:80/response

```
{
    "text":"Who is the hero of the story?"
}
```

## Docker
```
docker build -t chatgpt-project-one .
docker run -d -p 8080:80 chatgpt-project-one
```

## Kubernetes
```
kubectl get pods
kubectl apply -f pod.yaml
```