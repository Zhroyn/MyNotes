
- [Deep Learning](#deep-learning)
  - [Linear Classfier](#linear-classfier)
  - [Neural Network](#neural-network)
    - [Activation Functions](#activation-functions)
    - [Perceptron](#perceptron)
    - [Multi-layer Perceptron](#multi-layer-perceptron)
  - [Convolutional Neural Network](#convolutional-neural-network)
    - [Convolution Layer](#convolution-layer)
    - [Pooling Layer](#pooling-layer)
  - [Training Neural Network](#training-neural-network)
    - [Backpropagation](#backpropagation)
    - [Stochastic Gradient Descent (SGD)](#stochastic-gradient-descent-sgd)
    - [Cross Validation and Early Stop](#cross-validation-and-early-stop)
    - [Regularization and Dropout](#regularization-and-dropout)
    - [Data Augmentation](#data-augmentation)
    - [Batch Normalization](#batch-normalization)








## Deep Learning
### Linear Classfier
Define the **score** as
$$f_w(x) = w^T x + b$$

where $x$ is the image, $w$ is the weights.

When $x$ is similar to $w$, the score is large. Then we can convert scores to probabilities by **softmax** function
$$\sigma(\bold{z})_j = \frac{e^{z_j}}{\sum_{k=1}^{K} e^{z_k}}$$

Then we can use **cross entropy function** as loss function
$$H(P, Q) = -\sum_i P_i \log Q_i$$

where $P$ is the true probabilities, $Q$ is the predicted probabilities.








<br>

### Neural Network
#### Activation Functions
A activation function is to transform the summed weighted input and bias into an output value, which can be represented by
$$f(x) = \sigma(w^Tx + b)$$

For multiple outputs, we can use
$$f(x) = \sigma(Wx + b) $$

Rectified Linear Unit (ReLU):
$$\sigma(z) = \max(0, z)$$

Sigmoid:
$$\sigma(z) = \frac{1}{1 + e^{-z}}$$

<br>

#### Perceptron
A perceptron is an artificial neuron using the Heaviside step function as the activation function. The perceptron algorithm is also termed the single-layer perceptron. It can be represented by
$$
f(x) = \begin{cases}
  1 & \text{if } w^Tx + b > 0 \\
  0 & \text{otherwise}
\end{cases}
$$

<br>

#### Multi-layer Perceptron
A multi-layer perceptron (MLP) is a fully connected class of feedforward artificial neural network. In a fully connected layer, nodes are fully connected to the nodes in the previous layer.

An MLP consists of at least three layers of nodes: an input layer, a hidden layer and an output layer. Except for the input nodes, each node is a neuron that uses a nonlinear activation function.








<br>

### Convolutional Neural Network
A convolutional neural network (CNN) is a **locally connected network**. CNNs use a mathematical operation called convolution in place of general matrix multiplication in at least one of their layers.

<br>

#### Convolution Layer
The input of a convolution layer is an image, and the parameters is the convolution **kernels** or **filters** that slide along input features and provide translation-equivariant responses known as **feature maps** (**activation maps**).

The size of output is: ImageSize – FilterSize + 1
To change the size of output, we can use padding (adding zero pixels around the border) or stride (step size larger than 1 in convolution).
Then the size of output is: (ImageSize – FilterSize + Padding * 2) / Stride + 1

For multi-channel image, filters always extend the full depth of the input volume. And for multiple outputs, we can add the number of filters. The number of filters is the number of feature maps.

For a convolution layer with kernel size $K$, each element in the output depends on a $K \times K$ receptive field in the input.
For successive convolution with $K$ kernel size and $L$ layers, the receptive field is $1 + L * (K – 1)$

<br>

#### Pooling Layer
A pooling layer can combine outputs of a filter at different locations. It can aggregate spatial information and make feature maps smaller and more manageable.

Pooling operators:
- Max pooling
- Average pooling








<br>

### Training Neural Network
#### Backpropagation
Define a CNN as a composition of functions
$$f_{\bm{w}}(\bm{x}) = f_L(\dots(f_2(f_1(\bm{x};\bm{w}_1);\bm{w}_2)\dots;\bm{w}_L))$$

Its parameter is
$$\bm{w} = (\bm{w}_1, \bm{w}_2, \dots, \bm{w}_L)$$

Its loss function is
$$L(\bm{w}) = \frac{1}{n} \sum_i l(y_i, f_{\bm{w}}(\bm{x}_i))$$

where $y_i$ are its true training labels, $f_{\bm{x}}(\bm{x}_i)$ are its estimated labels. Then the gradient descent is

$$\bm{w}^{t+1} = \bm{w}^t - \eta_t \frac{\partial L}{\partial \bm{w}}(\bm{w}^t)$$

where $\eta_t$ are learing rates.

<br>

#### Stochastic Gradient Descent (SGD)
Stochastic gradient descent only calcualte loss and gradients on a batch of randomly sampled images, that is,
$$
\hat{L}(\bm{w}) = \frac{1}{n} \sum_{i\in \Omega} l(y_i, f_{\bm{w}}(\bm{x}_i)) \\~\\
SG = \frac{\partial \hat{L}}{\partial \bm{w}}(\bm{w}^t)
$$

Stochastic gradients approximate the real gradients.

<br>

#### Cross Validation and Early Stop
We often split data into train, validation and test sets. This method is called **cross validation**.

The model is initially fit on the **train set**.
Then, the fitted model is used to predict the responses on the **validation set**, the result of which is used to tune the model's hyperparameters. When the validation loss begins to increase, it's usually the time to early stop.
Finally, the **test set** is used to provide an evaluation of the final model fit.

<br>

#### Regularization and Dropout
To avoid overfitting, we may hope less or smaller parameters, so here comes regularization.

One method is to explicitly add a term to the optimization problem
$$L = \frac{1}{N}\sum_{i=1}^{N} \sum_{j\neq y_i}\max(0, f(\bm{x}_i;W)_j - f(\bm{x}_i;W)_{y_i} + 1) + \lambda R(W)$$

- L1: $R(W) = \sum_i \sum_j |W_{ij}|$
- L2: $R(W) = \sum_i \sum_j W_{ij}^2$

Another method is to randomly omit some weights during the training process, which is called **dropout**.

<br>

#### Data Augmentation
Another way to avoid overfitting is to largen the data set. We can do this by changing brightness of images, rollovering images, randomly cropping and scaling images, etc.

<br>

#### Batch Normalization
We also often normalize the outputs of a layer so they have zero mean and unit variance
$$\hat{x}^{(k)} = \frac{x^{(k)} - E[x^{(k)}]}{\sqrt{\text{Var}[x^{(k)}]}}$$

It makes neural network much easier to train, more robust to initialization, and allows higher learning rate and faster convergence.


