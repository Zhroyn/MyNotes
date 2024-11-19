
## Deep Learning
### Linear Classfier
Define the **score** as

$$f_w(x) = w^T x + b$$

where $x$ is the image, $w$ is the weights.

When $x$ is similar to $w$, the score is large. Then we can convert scores to probabilities by **softmax** function

$$\sigma(\mathbf{z})_j = \frac{e^{z_j}}{\sum_{k=1}^{K} e^{z_k}}$$

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

- Sigmoid: $\sigma(x) = \frac{1}{1 + e^{-x}}$
    - Problems: Saturated neurons kill the gradients; outputs are not zero-centered; compute expensive
- tanh: $\tanh(x) = \frac{e^x - e^{-x}}{e^x + e^{-x}}$
    - Advantages: zero centered
    - Problems: still kills gradients when saturated
- Rectified Linear Unit (ReLU): $\max(0, x)$
    - Advantages: Does not saturate; Very computationally efficient; Converges much faster than sigmoid/tanh in practice
    - Problems: Not zero-centered; big learning rate may cause dead ReLU problem 
- Leaky ReLU or Parametric Rectifier (PReLU, $\alpha$ is learned): $\max(0.01x, x), \quad \max(\alpha x, x)$
    - Advantages: Does not saturate; Computationally efficient; Converges much faster than sigmoid/tanh in practice; will not die
    - Problems: Not zero-centered; big learning rate may cause dead ReLU problem 
- Exponential Linear Unit (ELU): $\begin{cases} x & x \gt 0 \\ \alpha(e^x - 1) & x \le 0 \end{cases}$
    - Advantages: All benefits of ReLU; Closer to zero mean outputs; Negative saturation regime compared with Leaky ReLU adds some robustness to noise
    - Problems: Computation requires exp()
- Scaled Exponential Linear Unit (SELU): $\begin{cases} \lambda x & x \gt 0 \\ \lambda\alpha(e^x - 1) & x \le 0 \end{cases}$
    - Advantages: Works better for deep networks; "Self-normalizing" property; Can train deep SELU networks without BatchNorm
- Maxout: $\max(w_1^Tx + b_1, w_2^Tx + b_2)$
    - Advantages: Generalizes ReLU and Leaky ReLU; Linear Regime; Does not saturate; Does not die
    - Problems: Doubles the number of parameters/neuron

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

For multi-channel image, filters always extend to the full depth of the input volume, and only output one featur map.
For multiple outputs, we can add the number of filters. The number of filters is the number of feature maps.

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

Its parameter is $\bm{w} = (\bm{w}_1, \bm{w}_2, \dots, \bm{w}_L)$, and its loss function is

$$L(\bm{w}) = \frac{1}{n} \sum_i l(y_i, f_{\bm{w}}(\bm{x}_i))$$

where $y_i$ are its true training labels, $f_{\bm{x}}(\bm{x}_i)$ are its estimated labels. Then the gradient descent is

$$\bm{w}^{t+1} = \bm{w}^t - \eta_t \frac{\partial L}{\partial \bm{w}}(\bm{w}^t)$$

where $\eta_t$ are learing rates.

In practice, we usually only use Stochastic Gradient Descent (SGD), which only calcualte loss and gradients on a batch of randomly sampled images, that is,

$$
\hat{L}(\bm{w}) = \frac{1}{n} \sum_{i\in \Omega} l(y_i, f_{\bm{w}}(\bm{x}_i)) \\~\\
SG = \frac{\partial \hat{L}}{\partial \bm{w}}(\bm{w}^t)
$$

Stochastic gradients approximate the real gradients.

---
Here is a simple example of backpropagation. For $f(x, W) = \left\| W \cdot x \right\|^2 $, let $q = W \cdot x$, then the gradient is 

$$
q_k = \sum_j W_{k,j} x_j
\\~\\
\frac{\partial f}{\partial W_{i, j}} = \sum_k \frac{\partial f}{\partial q_k} \frac{\partial q_k}{\partial W_{i, j}} = 2q_i x_j
\quad \Rightarrow \quad \nabla_W f = 2q \cdot x^T
\\~\\
\frac{\partial f}{\partial x_j} = \sum_k \frac{\partial f}{\partial q_k} \frac{\partial q_k}{\partial x_j} = \sum_k 2q_k W_{k,j}
\quad \Rightarrow \quad \nabla_x f = 2W^T \cdot q
$$

Furthermore, for $f(x) = \left\| \tanh(W_2 \cdot \tanh(W_1 x + b_1) + b_2) \right\|^2 $, let's suppose

$$
y_1 = W_1 x + b_1, y_2 = \tanh y_1, \\
y_3 = W_2 y_2 + b_2, y_4 = \tanh y_3
$$

Then we can get

$$
\frac{\partial f}{\partial y_3} = 2(1 + y_4)(1 - y_4),
\quad \frac{\partial f}{\partial y_2} = W_2^T \cdot \nabla_{y_3} f,
\quad \frac{\partial f}{\partial W_2} = \nabla_{y_3} f \cdot y_2^T
\\~\\
\frac{\partial f}{\partial y_1} = \nabla_{y_2} f \odot (1 + y_2)(1 - y_2),
\quad \frac{\partial f}{\partial x} = W_1^T \cdot \nabla_{y_1} f,
\quad \frac{\partial f}{\partial W_1} = \nabla_{y_1} f \cdot x^T
$$

<br>

#### Optimizer
**SGD with Momentum**

$$
v_{t+1} = \rho v_t - \alpha \nabla f(x_t) \\
x_{t+1} = x_t + v_{t+1}
$$

The typical value of $\rho$ is about 0.9. When cross-validated, this parameter is usually set to values such as [0.5, 0.9, 0.95, 0.99].
Optimization can sometimes benefit a little from momentum schedules, where the momentum is increased in later stages of learning. A typical setting is to start with momentum of about 0.5 and anneal it to 0.99 or so over multiple epochs.

**Nesterov Momentum**

$$
\begin{aligned}
  v_{t+1} &= \rho v_t - \alpha \nabla f(x_t + \rho v_t) \\
  x_{t+1} &= x_t + v_{t+1}
\end{aligned}
$$

To update in terms of $x_t, \nabla f(x_t)$, we can set $\tilde{x}_t = x_t + \rho v_t$ and rearrange:

$$
\begin{aligned}
  v_{t+1} &= \rho v_t - \alpha \nabla f(\tilde{x}) \\
  \tilde{x}_{t+1} &= \tilde{x}_t - \rho v_t + (1 + \rho)v_{t+1} \\
  &= \tilde{x}_t + v_{t+1} + \rho(v_{t+1} - v_t)
\end{aligned}
$$

**AdaGrad**

```py
cache += dx**2
x += - learning_rate * dx / (np.sqrt(cache) + eps)
```

Adagrad is an **adaptive learning rate method**. The weights that receive high gradients will have their effective learning rate reduced, while weights that receive small or infrequent updates will have their effective learning rate increased.
A downside of Adagrad is that in case of deep learning, the monotonic learning rate usually proves too aggressive and stops learning too early.

**RMSProp**

```py
cache = decay_rate * cache + (1 - decay_rate) * dx**2
x += - learning_rate * dx / (np.sqrt(cache) + eps)
```
decay_rate is a hyperparameter and typical values are [0.9, 0.99, 0.999].

**Adam**

```py
m = beta1*m + (1-beta1)*dx
v = beta2*v + (1-beta2)*(dx**2)
x += - learning_rate * m / (np.sqrt(v) + eps)
```
Recommended values in the paper are eps = 1e-8, beta1 = 0.9, beta2 = 0.999.
The full Adam update also includes a bias correction mechanism, which compensates for the fact that in the first few time steps the vectors m,v are both initialized and therefore biased at zero:

```py
m = beta1*m + (1-beta1)*dx
mt = m / (1-beta1**t)
v = beta2*v + (1-beta2)*(dx**2)
vt = v / (1-beta2**t)
x += - learning_rate * mt / (np.sqrt(vt) + eps)
```

<br>

#### Weight Initialization
##### Xavier Initialization
Let $s = \sum_i^n w_i x_i$, assume $E(w) = 0, E(x) = 0$, then the variance of $s$ is

$$
\begin{aligned}
  \text{Var}(s) &= \text{Var}(\sum_i^n w_i x_i) \\
  &= \sum_i^n \text{Var}(w_ix_i) \\
  &= \sum_i^n [E(w_i)]^2\text{Var}(x_i) + [E(x_i)]^2\text{Var}(w_i) + \text{Var}(x_i)\text{Var}(w_i) \\
  &= \sum_i^n \text{Var}(x_i)\text{Var}(w_i) \\
  &= (n \text{Var}(w)) \text{Var}(x) \\
\end{aligned}
$$

Because $\text{Var}(aX) = a^2\text{Var}(X)$, to keep $\text{Var}(s) = \text{Var}(x)$, we can initialize with
```py
W = np.random.randn(Din, Dout) / np.sqrt(Din)
```
For conv layers, Din is filter_size^2 * input_channels

<br>

##### Kaiming Initialization
In the ReLU network, it is assumed that half of the neurons in each layer are activated and the other half is 0, to maintain the variance, simply divide by 2 based on Xavier

```py
W = np.random.randn(Din, Dout) / np.sqrt(2/Din)
```

<br>

#### Batch Normalization
We often do batch normalization to the outputs of a layer before the activation function so they have zero mean and unit variance.

To do this, we firstly compute the empirical mean and variance independently for each dimension and then normalize:

$$\hat{x}^{(k)} = \frac{x^{(k)} - E[x^{(k)}]}{\sqrt{\text{Var}[x^{(k)}] + \epsilon}}$$

Here $x$ is the values of the same dimension from different training examples in a mini-batch. As for convolutional layers, we normalize not only across all the training examples, but also cross the whole activation map, that is, per activation map have one mean and one standard deviation in a mini-batch.

Then, the network can still learn to change the distribution by

$$y^{(k)} = \gamma^{(k)} \hat{x}^{(k)} + \beta^{(k)}$$

Batch Normalization makes neural network much easier to train, more robust to initialization, allows higher learning rate and faster convergence, and acts as a form of regularization due to the randomness of the mean and variance of each mini-batch.

<br>

#### Regularization
To avoid overfitting, we may hope less or smaller parameters, so here comes regularization.

**L1 and L2 Regularization**
One method is to add a regularization term to the loss function

$$L(W) = \frac{1}{N}\sum_{i=1}^{N} L_i(f(x_i, W), y_i) + \lambda R(W)$$

- **L1 regularization**: $R(W) = \sum_i \sum_j |W_{ij}|$
    - L1 regularization tends to generate sparse solutions, that is, causing more weights to become 0
- **L2 regularization**: $R(W) = \sum_i \sum_j W_{ij}^2$
    - L2 regularization likes to spread out the weights
- Elastic net (L1 + L2): $R(W) = \sum_i \sum_j \beta W_{ij}^2 + |W_{ij}|$

**Max Norm Constraints**
Another form of regularization is to enforce an absolute upper bound on the magnitude of the weight vector for every neuron, and use projected gradient descent to enforce the constraint.
In practice, this corresponds to performing the parameter update as normal, and then enforcing the constraint by clamping the weight vector $w$ of every neuron to satisfy $\left\| w \right\|_2 < c$. Typical values of $c$ are on orders of 3 or 4.

**Dropout**
While training, we keep a neuron active with some probability $p$, or set it to zero otherwise.
While predicting, we need to multiply the output of neurons by $p$ to have the same output as they had during training time.
To make the model predict faster, we can use **inverted dropout**, that is, scale the output of neurons with $1/p$ during training time, leaving the forward pass at test time untouched.

<br>

#### Data Augmentation
Another way to avoid overfitting is to largen the data set. We can do this by changing brightness of images, rollovering images, randomly cropping and scaling images, etc.










<br>

### Babysitting Learning
#### Sanity Check
First, before the formal training, we can initialize the network, do a forward pass through it and make sure the loss is reasonable (with and without regularization).

As a second sanity check, increasing the regularization strength should increase the loss.

Then, we can overfit a tiny subset of data, and make sure we can achieve zero cost (without regularization).

<br>

#### Hyperparameter Optimization
The most common hyperparameters in context of Neural Networks include:

- Initial learning rate
- Learning rate decay schedule (such as the decay constant)
- Regularization strength (L2 penalty, dropout strength)

First, start to find a suiable learning rate with small regularization. If the training takes a long time, we can decide it by watching loss curve:
If the loss barely change, the lr is too low; if the loss change sharply, the lr is too high;
If there is a steep fall but then a high plateau, the lr may be too high;
If the loss curve keeps flat for a while and then start descending suddenly, it may be due to bad initialization.

For other hyperparameters, we'd better use **cross validation**. We can firstly run coarse search for a few epochs and then run fine search.
For learning rate, it's best to run coarse search in log space.
For multiple hyperparameters, it's a better method to do hyperparameters optimization by random search.

If the gap between the benchmark of train set and validation set is too big, it indicates the network is overfitting, we can increase regularization strength. If there is no gap, it indicates we may be able to increase model capacity.

During the training process, we can also watch the ratio between updated values and initial weights, which is expected to be somewhere around 0.001 or so.

