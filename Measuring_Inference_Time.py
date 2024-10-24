import time

def inference_function(model):
    start_time = time.time()
    time.sleep(0.08)  # Simulating a delay for inference
    end_time = time.time()
    
    inference_time = end_time - start_time
    return inference_time

inference_time_before = inference_function('fine_tuned_model.pt')
inference_time_after = inference_function('quantized_model.pt')

print(f"Inference Time Before Quantization: {inference_time_before:.2f} seconds")
print(f"Inference Time After Quantization: {inference_time_after:.2f} seconds")
