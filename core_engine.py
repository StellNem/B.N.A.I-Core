import ollama

# Default local connection
ollama_client = ollama.Client(host="http://127.0.0.1:11434")
MODEL_NAME = "qwen2.5:7b"

def run_agent_loop(messages, status_callback=None):
    """A lightweight local inference connector for the open-source template."""
    if status_callback:
        status_callback("Connecting to local model...")
    
    # Simple system prompt injection
    has_system = False
    for msg in messages:
        if msg["role"] == "system":
            has_system = True
            break
            
    if not has_system:
        messages.insert(0, {
            "role": "system",
            "content": "You are Bardie Core, a brilliant local AI partner. Run entirely locally."
        })

    response = ollama_client.chat(
        model=MODEL_NAME,
        messages=messages
    )
    
    return response['message']['content']