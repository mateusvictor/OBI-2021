#!/usr/bin/env python2.7
# chuva, dfs, OBI-2019

def dfs( i, j ):
    # molha
    p[i][j] = 'o'

    # base
    if ( i == N-1 ): return

    # recusao
    if ( p[i+1][j] == '.' ): dfs( i+1, j )
    if ( p[i+1][j] == '#' ):
        if ( p[i][j-1] == '.' ): dfs( i, j-1 )
        if ( p[i][j+1] == '.' ): dfs( i, j+1 )
        

N,M = [int(i) for i in input().split()]
        
p = []
for i in range(N):
    p.append(list(input()))

dfs( 0, p[0].index('o') )

for i in range(N):
    print(''.join(p[i]))
    