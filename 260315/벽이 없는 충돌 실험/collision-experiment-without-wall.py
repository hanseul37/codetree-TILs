import sys

# 입력 속도 최적화
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    beads = [] 
    
    for i in range(n):
        xi, yi, wi, di = input().split()
        x = (int(xi) + 1000) * 2
        # 🚨 여기에 빠졌던 마이너스(-) 부호를 복구했습니다!
        y = (-int(yi) + 1000) * 2 
        w = int(wi)
        beads.append([x, y, w, di, i]) 

    last_collision = -1
    
    for cnt in range(1, 4001):
        if len(beads) <= 1:
            break
            
        pos = {}
        is_collided = False
        
        for b in beads:
            if b[3] == 'U': b[1] -= 1
            elif b[3] == 'D': b[1] += 1
            elif b[3] == 'R': b[0] += 1
            elif b[3] == 'L': b[0] -= 1
            
            key = (b[0], b[1])
            
            if key not in pos:
                pos[key] = b
            else:
                is_collided = True
                existing = pos[key]
                # 무게가 크거나, 무게가 같을 때 고유 번호가 큰 구슬이 생존
                if b[2] > existing[2] or (b[2] == existing[2] and b[4] > existing[4]):
                    pos[key] = b
                    
        if is_collided:
            last_collision = cnt
            
        beads = list(pos.values())

    print(last_collision)