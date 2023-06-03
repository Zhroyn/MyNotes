<!-- TOC -->

- [保存和加载模型](#保存和加载模型)
- [使用模型](#使用模型)

<!-- /TOC -->





### 保存和加载模型
```py
# 保存整个模型网络结构和参数
torch.save(model, path)

model = torch.load(path)
model.eval()

# 仅保存参数
model = nn.Model()
torch.save(model.state_dict(), path)

model = nn.Model()
model.load_state_dict(torch.load(path))
model.eval()
```


### 使用模型
```py
# 加载模型
model = models.resnet50(weights=models.ResNet50_Weights.DEFAULT)
model.eval()

# 图像预处理
norm_mean = [0.485, 0.456, 0.406]
norm_std = [0.229, 0.224, 0.225]

preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(norm_mean, norm_std),
])

img = Image.open(img_path)
img_tensor = preprocess(img)
img_input = img_tensor.unsqueeze(0)

# 获取标签
output = model(img_input)
predicted_index = torch.max(output, 1)[1]
predicted_label = labels[predicted_index.item()]
```

