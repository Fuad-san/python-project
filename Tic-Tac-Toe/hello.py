# height = 6

# for i in range(height):
#     for j in range(height - i - 1):
#         print(' ', end='')
#     for j in range( 2 * i + 1):
#         if j == 0 or j == 2 * i or i == height - 1:
#             print('*', end="")
#         else:
#             print(' ', end='')
#     print()
    

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import Lasso, Ridge
from sklearn.preprocessing import StandardScaler

# Create a small dataset
X = np.array([[1, 5],
              [2, 4],
              [3, 3],
              [4, 2],
              [5, 1]])
y = np.array([3, 3, 2, 5, 5])

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Fit linear regression with L1 regularization (Lasso)
lasso = Lasso(alpha=1.0)  # alpha is the regularization parameter (λ)
lasso.fit(X_scaled, y)
lasso_coefs = lasso.coef_

# Fit linear regression with L2 regularization (Ridge)
ridge = Ridge(alpha=1.0)  # alpha is the regularization parameter (λ)
ridge.fit(X_scaled, y)
ridge_coefs = ridge.coef_

# Plot the results
fig, ax = plt.subplots(1, 2, figsize=(12, 5))

# L1 Regularization (Lasso)
ax[0].bar(range(len(lasso_coefs)), lasso_coefs, color='blue', alpha=0.7)
ax[0].set_title('L1 Regularization (Lasso)')
ax[0].set_xlabel('Feature')
ax[0].set_ylabel('Coefficient Value')
ax[0].set_xticks(range(len(lasso_coefs)))
ax[0].set_xticklabels([f'Feature {i+1}' for i in range(len(lasso_coefs))])

# L2 Regularization (Ridge)
ax[1].bar(range(len(ridge_coefs)), ridge_coefs, color='green', alpha=0.7)
ax[1].set_title('L2 Regularization (Ridge)')
ax[1].set_xlabel('Feature')
ax[1].set_ylabel('Coefficient Value')
ax[1].set_xticks(range(len(ridge_coefs)))
ax[1].set_xticklabels([f'Feature {i+1}' for i in range(len(ridge_coefs))])

plt.tight_layout()
plt.show()