data = [
    4.842,
    4.842,
    4.842,
    1.093,
    4.503,
    4.503,
    4.503,
    4.503,
    4.503,
    4.503,
    4.503,
    4.503,
    4.503,
    4.503,
    4.503,
    4.503,
    4.503,
    9.137,
    9.137,
    9.137,
    9.137,
    9.137,
    9.137,
    9.137,
    9.137,
    9.137,
    9.137,
    9.137,
    9.137,
    9.137,
    9.137,
    12.1,
    12.1,
    12.1,
    1.093,
    12.18,
    12.18,
    12.18,
    12.18,
    12.18,
    12.18,
    12.18,
    12.18,
    12.18,
    12.18,
    12.18,
    12.18,
    12.18,
    12.18,
    12.18,
    12.18,
    12.18,
    12.18,
    12.18,
    12.18,
    12.18,
    12.18,
    12.18,
    12.18,
    12.18,
    12.18,
    12.18,
    12.18,
    12.18,
    12.18,
    12.18,
    12.18,
    11.476,
    11.476,
    11.476,
    11.476,
    11.476,
    1.748,
    11.56,
    11.56,
    11.56,
]

print("{deepkit: create-channel, name: accuracy, kpi: True, main: True}")
for i, v in enumerate(data):
    print("{deepkit: channel, name: accuracy, x: %d, y: %f}" %(i, v))

