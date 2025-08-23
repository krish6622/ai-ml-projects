import numpy as np
import matplotlib.pyplot as plt

# Our dataset
X = np.array([1.1, 1.3, 1.5, 2.0, 2.2, 2.9, 3.0, 3.2, 3.2, 3.7,
              3.9, 4.0, 4.0, 4.1, 4.5, 4.9, 5.1, 5.3, 5.9, 6.0,
              6.8, 7.1, 7.9, 8.2, 8.7, 9.0, 9.5, 9.6, 10.3, 10.5])
Y = np.array([3.9, 4.6, 3.7, 4.3, 3.9, 5.6, 6.0, 5.4, 6.4, 6.3,
              5.5, 5.6, 6.1, 5.7, 6.3, 6.6, 7.6, 6.0, 6.7, 8.3,
              8.1, 9.3, 8.7, 10.1, 9.6, 10.9, 10.5, 11.2, 11.2, 11.7])

#Step 1:Calculate means
X_mean=np.mean(X)
Y_mean=np.mean(Y)
print(f"Mean of Experience:{X_mean:.2f} years")
print(f"Mean of Salary:{Y_mean:.2f} lakhs")

#Step 2:Calculate slope using the formula
numerator=np.sum((X-X_mean)*(Y-Y_mean))
denominator=np.sum((X-X_mean)**2)
m=numerator/denominator
print(f"\nSlope calculation:")
print(f"Numerator: {numerator:.3f}")
print(f"Denominator: {denominator:.3f}")
print(f"Slope (m): {m:.3f}")

#Step 3:Calculate y-intercept
c=Y_mean-m*X_mean
print(f"\nY-intercept (c): {c:.3f}")

# Step 4: Display the equation
print(f"\nFinal equation: Y = {m:.3f}X + {c:.3f}")

#Step 5:Make Predictions
print("\nPredictions")
for exp in [0,2,5,8,12]:
    salary=m*exp+c
    print(f"Experience: {exp} years -> Salary: {salary:.2f} lakhs")

# Calculate R-squared to check model quality
Y_pred=m*X+c
ss_total=np.sum((Y-Y_mean)**2)
ss_residual=np.sum((Y-Y_pred)**2)
r_squared=1-(ss_residual/ss_total)

print(f"\nR-squared: {r_squared:.3f} (Model explains {r_squared*100:.1f}% of variance)")