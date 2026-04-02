import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

# ==============================
# 1. 加载 MNIST 手写数字数据集
# ==============================
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# 数据归一化 [0,255] → [0,1]
x_train = x_train / 255.0
x_test = x_test / 255.0

# 添加通道维度 (28,28) → (28,28,1)
x_train = x_train[..., tf.newaxis]
x_test = x_test[..., tf.newaxis]

print("训练数据形状：", x_train.shape)
print("测试数据形状：", x_test.shape)

# ==============================
# 2. 构建卷积神经网络 CNN 模型
# ==============================
model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(28,28,1)),
    tf.keras.layers.MaxPooling2D((2,2)),
    tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D((2,2)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')  # 输出 10 类
])

# ==============================
# 3. 编译模型
# ==============================
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# ==============================
# 4. 训练模型并记录训练过程
# ==============================
history = model.fit(x_train, y_train, epochs=5,
                    validation_data=(x_test, y_test),
                    batch_size=64)

# ==============================
# 5. 可视化训练过程（Loss & Accuracy）
# ==============================
plt.figure(figsize=(12,4))

# 训练 & 验证损失
plt.subplot(1,2,1)
plt.plot(history.history['loss'], label='Train Loss')
plt.plot(history.history['val_loss'], label='Val Loss')
plt.title('Training & Validation Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()

# 训练 & 验证准确率
plt.subplot(1,2,2)
plt.plot(history.history['accuracy'], label='Train Acc')
plt.plot(history.history['val_accuracy'], label='Val Acc')
plt.title('Training & Validation Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()

plt.show()

# ==============================
# 6. 模型评估
# ==============================
test_loss, test_acc = model.evaluate(x_test, y_test, verbose=0)
print(f"\n✅ 测试集准确率: {test_acc:.4f}")

# ==============================
# 7. 预测并展示结果
# ==============================
predictions = model.predict(x_test[:10])
predicted_labels = np.argmax(predictions, axis=1)

plt.figure(figsize=(10, 2))
for i in range(10):
    plt.subplot(1, 10, i+1)
    plt.imshow(x_test[i].reshape(28,28), cmap='gray')
    plt.title(f"P:{predicted_labels[i]}\nT:{y_test[i]}")
    plt.axis('off')
plt.tight_layout()
plt.show()
