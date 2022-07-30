import numpy

def make_prediction(image):
    import torch
    from torch.nn import Conv2d
    from torch.nn import Linear
    from torch.nn import MaxPool2d
    from torch.nn import ReLU
    from torch.nn import LogSoftmax
    from torch import flatten
    import torch.nn as nn
    import torch.nn.functional as F
    import torch.optim as optim
    from PIL import Image
    import torchvision.transforms as transforms
    PATH = r"C:\Users\EXG\OneDrive - Danmarks Tekniske Universitet\Skrivebord\Vue project 2\myNN2"

    class ConvNet(nn.Module):
        def __init__(self):
            super(ConvNet, self).__init__()
            self.conv1 = nn.Conv2d(3, 12, 3)
            self.conv2 = nn.Conv2d(12, 6, 3)

            #self.conv3 = nn.Conv2d(200, 400, 2)
            #self.conv4 = nn.Conv2d(400, 400, 2)

            self.pool = nn.MaxPool2d(2)

            self.fc1 = nn.Linear(23064, 1000)
            self.fc2 = nn.Linear(1000, 2)
            self.drop1 = nn.Dropout(p=0.1)
            self.drop2 = nn.Dropout(p=0.1)

        def forward(self, x):

            x = F.relu(self.conv1(x))
            x = self.pool(F.relu(self.conv2(x)))

            #x = F.relu(self.conv3(x))
            #x = self.pool(F.relu(self.conv4(x)))

            x = x.view(x.size(0), -1)
            x = self.drop1(x)
            x = F.relu(self.fc1(x))
            x = self.drop2(x)
            x = self.fc2(x)

            #x = F.softmax(x, dim=1)
            return x

    model = ConvNet()
    model.load_state_dict(torch.load(PATH))
    model.eval()

    #now to code pertaining to communication with javascript
    #image =
    #f = r'C:\Users\EXG\OneDrive - Danmarks Tekniske Universitet\Skrivebord\Vue project 2\Capture.jpg'
    #image = Image.open(f)  # if image.size != (512, 512):

    def data_prep(image):
        size = (128, 128)
        image = image.resize(size)
        transform = transforms.Compose([transforms.PILToTensor()])
        transform = transforms.PILToTensor()
        img_tensor = transform(image)
        img_tensor = torch.unsqueeze(img_tensor, dim=0)
        return img_tensor.float()
    image = data_prep(image)

    output = model(image)

    output = torch.argmax(F.softmax(output, dim=1))  # 0 is cat, 1 is dog

    if output == 0:
        prediction = 'Cat'
    elif output == 1:
        prediction = 'Dog'
    else:
        prediction = 'Error'

    print(prediction)

def printing():
    print("hello ")