#include <iostream>
#include <string>
using namespace std;

int main() {

	//copying cypher sequence from webpage
	int cipher[]= {183,12,2,219,22,194,143,234,5,221,14,8,208,27,11,219,8,10,216,22,4,226,199,252,222,25,
		182,226,22,2,229,16,4,214,199,10,215,12,182,182,8,3,209,16,10,143,10,254,208,19,2,212,21,253,212,
		213,182,191,19,251,208,26,251,143,26,251,221,11,182,232,22,11,225,199,9,222,19,11,227,16,5,221,199,
		247,221,11,182,178,253,182,227,22,182,216,10,247,221,10,5,211,12,214,214,8,3,209,16,10,225,12,9,212,
		8,8,210,15,196,210,22,3,143,24,11,222,27,255,221,14,182,225,12,252,212,25,251,221,10,251,169,199,252,
		162,224,207,165,223,206,165,215,250,157};

	const int cipher_length = 151;


	//from the webpage source we read the cypher function:
	// 	function scramble(ascii,a,b,c) {
	// 	for(i=0; i<ascii.length; i++) {
	// 		if (i%3==0) {ascii[i]=(ascii[i]+a)%256;}
	// 		if (i%3==1) {ascii[i]=(ascii[i]+b)%256;}
	// 		if (i%3==2) {ascii[i]=(ascii[i]+c)%256;}
	// 	}
	// 	return ascii;
	// }
	// this means that the message was coded by position dependent shift

	//brute-force approach trying all possibles values for a, b, c (because the space of possibles is relatively small, 256**3 here)
	for(int a=0; a < 255; ++a){
		for(int b=0; b < 255; ++b){
			for(int c=0; c < 255; ++c){
				char message[cipher_length];
				for (int i = 0 ; i < cipher_length; ++i) {
					message[i] = cipher[i];
					switch (i%3){
						case 0:
							message[i] -= a;
							break;
						case 1:
							message[i] -= b;
							break;
						case 2:
							message[i] -= c;
							break;
						}
					}

				//print out if "gambit" found in message (only happens for one combination)
				string s = message;
				if ( s.find("gambit") != string::npos){
					cout << s << endl;
					cout << "The cypher is a,b,c = " << a << "," << b << "," << c << endl;
					}
				}
			}
		}

	return 0;
}
