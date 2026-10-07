# -*- coding: utf-8 -*-
# Execute in a writable working directory: python main.py
# Requires numpy and matplotlib; all displayed blocks appear below in order.

# 002 온도 격자 자료의 입력과 공통 코드
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.size'] = 24
x = np.array([0, 1, 2, 3])
y = np.array([0, 1, 2])
Z = np.array([[20, 22, 24, 26],
              [22, 24, 26, 28],
              [24, 26, 28, 30]])
print(Z.shape, Z[0, 0], Z[2, 3])

# 003 좌표 격자와 온도 칸의 일대일 대응
X, Y = np.meshgrid(x, y)
print(X)
print(Y)
print(X.shape, Y.shape, Z.shape)

# 004 배열의 행 방향과 실제 좌표의 정렬
fig0, ax0 = plt.subplots(figsize=(6, 3))
im0 = ax0.imshow(Z, interpolation='nearest')
ax0.set(xlabel='column', ylabel='row')

# 004 배열의 행 방향과 실제 좌표의 정렬
extent = [-0.5, 3.5, -0.5, 2.5]
fig, ax = plt.subplots(figsize=(6, 3))
im = ax.imshow(Z, origin='lower',
    extent=extent, interpolation='nearest')
ax.set(xlabel='x (m)', ylabel='y (m)')

# 005 온도 구간과 기준 경계의 결합
fig, ax = plt.subplots(figsize=(7, 4))
cf = ax.contourf(X, Y, Z,
    levels=[20, 24, 28, 32], cmap='viridis')
cs = ax.contour(X, Y, Z,
    levels=[26], colors='black')
ax.clabel(cs, fmt='%d', fontsize=24)
fig.colorbar(cf, ax=ax, label='T (°C)')
ax.set(xlabel='x (m)', ylabel='y (m)')

# 006 히스토그램의 개수와 확률밀도
values = Z.ravel()
figN, axN = plt.subplots(figsize=(6, 3))
counts, edges, bars = axN.hist(values, bins=[20,24,32])
axN.set(xlabel='T (°C)', ylabel='Count')
print(counts)

# 006 히스토그램의 개수와 확률밀도
figD, axD = plt.subplots(figsize=(6, 3))
density, edges, bars = axD.hist(values,
    bins=[20,24,32], density=True)
axD.set(xlabel='T (°C)', ylabel='Density (1/°C)')
print(density)

# 007 2차원 집계 배열과 그림의 방향
px = [0, 1, 2, 3, 0, 1, 2, 3, 0, 1, 2, 3]
temperatures = Z.ravel()
fig, ax = plt.subplots(figsize=(7, 4))
H, xe, te, mesh = ax.hist2d(px, temperatures,
    bins=[[-0.5, 1.5, 3.5], [20, 24, 32]])
fig.colorbar(mesh, ax=ax, label='Count')
ax.set(xlabel='x (m)', ylabel='T (°C)')
print(H)

# 008 범례의 대상 이름과 위치
fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(x, Z[0], '-o', label='y=0 m')
ax.plot(x, Z[2], '--s', label='y=2 m')
ax.set(xlabel='x (m)', ylabel='T (°C)')
ax.legend()

# 008 범례의 대상 이름과 위치
ax.legend(loc='upper left', ncol=2,
    frameon=True)

# 009 값을 색으로 옮기는 기준과 컬러바
fig, ax = plt.subplots(figsize=(7, 4))
im = ax.imshow(Z, origin='lower', extent=extent,
    interpolation='nearest', cmap='viridis',
    vmin=20, vmax=30)
cb = fig.colorbar(im, ax=ax, label='T (°C)')
ax.set(xlabel='x (m)', ylabel='y (m)')
print(im.get_clim(), cb.mappable is im)

# 010 서로 다른 자동 색 범위의 비교
figA, axA = plt.subplots(figsize=(6, 3))
imA = axA.imshow(Z, origin='lower', extent=extent,
    interpolation='nearest', cmap='viridis')
figA.colorbar(imA, ax=axA, label='T (°C)')
axA.set(xlabel='x (m)', ylabel='y (m)')

# 010 서로 다른 자동 색 범위의 비교
B = Z + 2
figB, axB = plt.subplots(figsize=(6, 3))
imB = axB.imshow(B, origin='lower', extent=extent,
    interpolation='nearest', cmap='viridis')
figB.colorbar(imB, ax=axB, label='T (°C)')
axB.set(xlabel='x (m)', ylabel='y (m)')

# 011 공통 색 범위로의 변경
imA.set_clim(20, 32)

# 011 공통 색 범위로의 변경
imB.set_clim(20, 32)

# 012 기준 온도 대비 차이의 발산형 색상표
delta = Z - 24
fig, ax = plt.subplots(figsize=(7, 4))
im = ax.imshow(delta, origin='lower', extent=extent,
    interpolation='nearest', cmap='RdBu_r',
    vmin=-6, vmax=6)
fig.colorbar(im, ax=ax, label='T - 24 (°C)')
ax.set(xlabel='x (m)', ylabel='y (m)')

# 013 원본 값의 유지와 색 범위 초과 표시
C = Z.copy()
C[2, 3] = 60
fig, ax = plt.subplots(figsize=(7, 4))
im = ax.imshow(C, origin='lower', extent=extent,
    interpolation='nearest', cmap='viridis',
    vmin=20, vmax=30)
fig.colorbar(im, ax=ax, label='T (°C)', extend='max')
ax.set(xlabel='x (m)', ylabel='y (m)')
print(C.max(), Z.max())

# 014 2×2 subplot 배열과 Axes 선택
plt.close('all')
fig, axes = plt.subplots(2, 2, figsize=(7, 4),
    constrained_layout=True)
axes[0, 0].plot(x, Z[0])
axes[0, 0].set(xlabel='x (m)', ylabel='T (°C)')
print(axes.shape, len(fig.axes))

# 015 축 공유와 비교 단위의 일치
fig, axes = plt.subplots(2, 1, figsize=(7, 5),
    sharex=True, sharey=True)
axes[0].plot(x, Z[0], '-o')
axes[1].plot(x, Z[2], '--s')
axes[0].set(xlim=(0, 3), ylim=(18, 32),
    ylabel='T (°C)')
axes[1].set(xlabel='x (m)', ylabel='T (°C)')
print(axes[1].get_xlim(), axes[1].get_ylim())
