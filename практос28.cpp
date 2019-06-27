#include <iostream>
using std :: cout;
using std :: cin;
int main(){
	int a;
	cout << "Input a:";
	cin >> a;
	for (int y=0; y<a; y++){
		for (int x=0; x<a; x++)
		if (x<=y)
		cout << "*";
		else
		cout << " ";
		cout << "\n";
	}
}
