n, q = map(int, input().split())

dist = {
    "Seoul": 0.0,
    "Yeongdeungpo": 9.1,
    "Anyang": 23.9,
    "Suwon": 41.5,
    "Osan": 56.5,
    "Seojeongri": 66.5,
    "Pyeongtaek": 75.0,
    "Seonghwan": 84.4,
    "Cheonan": 96.6,
    "Sojeongni": 107.4,
    "Jeonui": 114.9,
    "Jochiwon": 129.3,
    "Bugang": 139.8,
    "Sintanjin": 151.9,
    "Daejeon": 166.3,
    "Okcheon": 182.5,
    "Iwon": 190.8,
    "Jitan": 196.4,
    "Simcheon": 200.8,
    "Gakgye": 204.6,
    "Yeongdong": 211.6,
    "Hwanggan": 226.2,
    "Chupungnyeong": 234.7,
    "Gimcheon": 253.8,
    "Gumi": 276.7,
    "Sagok": 281.3,
    "Yangmok": 289.5,
    "Waegwan": 296.0,
    "Sindong": 305.9,
    "Daegu": 323.1,
    "Dongdaegu": 326.3,
    "Gyeongsan": 338.6,
    "Namseonghyeon": 353.1,
    "Cheongdo": 361.8,
    "Sangdong": 372.2,
    "Miryang": 381.6,
    "Samnangjin": 394.1,
    "Wondong": 403.2,
    "Mulgeum": 412.4,
    "Hwamyeong": 421.8,
    "Gupo": 425.2,
    "Sasang": 430.3,
    "Busan": 441.7,
}

train = {}
for _ in range(n):
    name, st, et = input().split()
    train[name] = [st, et]

for _ in range(q):
    ss, es = input().split()
    d = dist[es] - dist[ss]
    st = train[ss][1]
    et = train[es][0]
    sh, sm = map(int, st.split(':'))
    eh, em = map(int, et.split(':'))
    start_time = sh * 60 + sm
    end_time = eh * 60 + em
    if start_time > end_time:
        total_time = 24 * 60 - start_time + end_time
    else:
        total_time = end_time - start_time
    print(abs(60 * d / total_time))