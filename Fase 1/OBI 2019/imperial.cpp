#include <bits/stdc++.h>

using namespace std;
const int maxn = 510;
int v[maxn];

int main() {
	ios::sync_with_stdio(false), cin.tie(0); // OTIMIZAÇÃO DO CIN/COUT
	int n;
	cin >> n;
	for (int i = 1; i <= n; i++) {
		cin >> v[i];
	}

	int ans = 0;
	for (int i = 1; i <= n; i++) {
		for (int j = i; j <= n; j++) {
			int a = v[i], b = v[j]; // A e B são os valores que iremos testar

			int ultimo = -1; // Ultimo cara que foi adicionado ( no inicio nenhum )
			int resp_local = 0; // Resposta para os valores de A e B
			for(int k = 1; k <= n; k++) {
				if (v[k] != a && v[k] != b || v[k] == ultimo) continue;
					// Se o valor na posição k for diferente de A ou de B ou então for igual ao úlitmo basta ignorá-lo.
				resp_local++; // Adiciono o valor na posição k na resposta de A e B
				ultimo = v[k]; // Guardo que ele foi o último adicionado
			}
			ans = max(ans, resp_local);
		}
	}
	cout << ans << "\n";

	return 0;
}