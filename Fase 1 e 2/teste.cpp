#include <bits/stdc++.h>

using namespace std;

#define ff first
#define ss second

typedef pair<int, int> pii;

const int maxn = 2e3+10;

int n;
int x[maxn], y[maxn];

int mx[maxn];

int dp[maxn][maxn];

// distância euclidiana entre as tendas i e j
int dist(int i, int j)
{
	int dx = x[i]-x[j];
	int dy = y[i]-y[j];

	return (dx*dx + dy*dy);
}

// função auxiliar para ordenar os pares de tendas pela distância
bool comp(pii a, pii b)
{
	return dist(a.ff, a.ss) < dist(b.ff, b.ss);
}

int main(void)
{
	system("cls");
	scanf("%d", &n);

	for (int i = 1; i <= n; i++)
		scanf("%d %d", &x[i], &y[i]);

	// vector que guarda os pares de tendas ordenados pela distancia
	vector<pii> par;

	// inserimos os pares no vector
	for (int i = 0; i <= n; i++)
		for (int j = 1; j <= n; j++)
			if (i != j)
				par.push_back({i, j});

	// em seguida, ordenamo-os
	sort(par.begin(), par.end(), comp);

	for (auto x : par)
		cout << "(" << x.ff << " ," << x.ss << ")\n";

	system("pause");
}