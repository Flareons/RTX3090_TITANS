import torch

print("Training completed!")

torch.save(
    model.state_dict(),
    "model_weight_save/TITANS_model.pth"
)

print("Model weights saved!")