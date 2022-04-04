#include<stdio.h>
#include<string.h>
#include<stdlib.h>
void  distance(char*ch, char c) {
	int num = strlen(ch);//字符串的长度
	int distance1=0, distance2=0, distance=0;
	for (int n = 0; n < num; n++) {
		for (int i = 0; i < num - n; i++) {
			if (ch[n + i] != 'e') {
				distance1 = 100;
			}//防止没找到e
			else if (ch[n + i] == 'e') {
				distance1 = i;
				break;
			}
		}//往右
		for (int j = 0; j <= n; j++) {
			if (ch[n - j] != 'e') {
				distance2 =100;
			}//防止没找到e
			else if (ch[n - j] == 'e') {
				distance2 = j;
				break;
			}
		}//往左
		distance = (distance1 <distance2) ? distance1: distance2;
		printf("%d", distance);
	}
}
int main() {
	char ch[20];
	gets_s(ch);
	distance(ch, 'e');
}