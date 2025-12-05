from langchain_huggingface import HuggingFacePipeline

# 方式一：直接加载预训练模型（本地运行）
llm = HuggingFacePipeline.from_model_id(    
    model_id="meta-llama/Llama-3.2-3B-Instruct",
    task="text-generation",
    device=-1,
    pipeline_kwargs={
        "max_new_tokens": 100,
        "temperature": 0.1,
        "top_k": 50
    }
)
res = llm.invoke("HELLO, HOW ARE YOU?")
print(res)