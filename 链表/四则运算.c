#include<stdio.h>
#include<stdlib.h>
void yue_fen(long long int* zi, long long int* mu, long long int* k)
{
	*k = *zi / *mu;//假分数的外值
	if (*k != 0)//该有理数>1
	{
		*zi = llabs(*zi % *mu);//llasb是取绝对值
	}
	else
	{
		*zi = *zi % *mu;
	}
	*mu = llabs(*mu);
	for (int i = 10; i >= 2; i--)//开始约分到最简形式
	{
		if (0 == (*zi % i) && 0 == (*mu % i))
		{
			*zi = *zi / i;
			*mu = *mu / i;
			i = 11;
		}
	}
}
void sum(long long int a1, long long int b1, long long int a2, long long int b2)//加法
{
	long long int resu_k, resu_a, resu_b, k1, k2;
	char ch = '+';
	if (0 == a1)//和
	{
		resu_a = a2;
		resu_b = b2;
	}
	else if (0 == a2)
	{
		resu_a = a1;
		resu_b = b1;
	}
	else
	{
		resu_a = a1 * b2 + a2 * b1;
		resu_b = b1 * b2;
	}
	yue_fen(&resu_a, &resu_b, &resu_k);//和
	yue_fen(&a1, &b1, &k1);
	yue_fen(&a2, &b2, &k2);//分子分母有理化
	if (0 == a1)								//判断第一个有理数
	{
		if (k1 < 0)
			printf("(%lld)", k1);
		else
			printf("%lld", k1);
	}
	else
	{
		if (0 == k1)
		{
			if (a1 > 0)
				printf("%lld/%lld", a1, b1);
			else
				printf("(%lld/%lld)", a1, b1);
		}
		else if (k1 < 0)
			printf("(%lld %lld/%lld)", k1, a1, b1);
		else
			printf("%lld %lld/%lld", k1, a1, b1);
	}
	printf(" %c ", ch);
	if (0 == a2)								//判断第二个有理数
	{
		if (k2 < 0)
			printf("(%lld)", k2);
		else
			printf("%lld", k2);
	}
	else
	{
		if (0 == k2)
		{
			if (a2 > 0)
				printf("%lld/%lld", a2, b2);
			else
				printf("(%lld/%lld)", a2, b2);
		}
		else if (k2 < 0)
			printf("(%lld %lld/%lld)", k2, a2, b2);
		else
			printf("%lld %lld/%lld", k2, a2, b2);
	}
	printf(" = ");
	if (0 == resu_a)								//判断结果
	{
		if (resu_k < 0)
			printf("(%lld)\n", resu_k);
		else
			printf("%lld\n", resu_k);
	}
	else
	{
		if (resu_k < 0)
			printf("(%lld %lld/%lld)\n", resu_k, resu_a, resu_b);
		else if (0 == resu_k && resu_a > 0)
			printf("%lld/%lld\n", resu_a, resu_b);
		else if (0 == resu_k && resu_a < 0)
			printf("(%lld/%lld)\n", resu_a, llabs(resu_b));
		else
			printf("%lld %lld/%lld\n", resu_k, resu_a, resu_b);
	}
}
void subtraction(long long int a1, long long int b1, long long int a2, long long int b2) {
	long long int resu_k, resu_a, resu_b, k1, k2;
	char ch = '-';
	if (0 == a1)//差
	{
		resu_a = a2;
		resu_b = b2;
	}
	else if (0 == a2)
	{
		resu_a = a1;
		resu_b = b1;
	}
	else
	{
		resu_a = a1 * b2 - a2 * b1;
		resu_b = b1 * b2;
	}
	yue_fen(&resu_a, &resu_b, &resu_k);//差
	yue_fen(&a1, &b1, &k1);
	yue_fen(&a2, &b2, &k2);//分子分母有理化
	if (0 == a1)								//判断第一个有理数
	{
		if (k1 < 0)
			printf("(%lld)", k1);
		else
			printf("%lld", k1);
	}
	else
	{
		if (0 == k1)
		{
			if (a1 > 0)
				printf("%lld/%lld", a1, b1);
			else
				printf("(%lld/%lld)", a1, b1);
		}
		else if (k1 < 0)
			printf("(%lld %lld/%lld)", k1, a1, b1);
		else
			printf("%lld %lld/%lld", k1, a1, b1);
	}
	printf(" %c ", ch);
	if (0 == a2)								//判断第二个有理数
	{
		if (k2 < 0)
			printf("(%lld)", k2);
		else
			printf("%lld", k2);
	}
	else
	{
		if (0 == k2)
		{
			if (a2 > 0)
				printf("%lld/%lld", a2, b2);
			else
				printf("(%lld/%lld)", a2, b2);
		}
		else if (k2 < 0)
			printf("(%lld %lld/%lld)", k2, a2, b2);
		else
			printf("%lld %lld/%lld", k2, a2, b2);
	}
	printf(" = ");
	if (0 == resu_a)								//判断结果
	{
		if (resu_k < 0)
			printf("(%lld)\n", resu_k);
		else
			printf("%lld\n", resu_k);
	}
	else
	{
		if (resu_k < 0)
			printf("(%lld %lld/%lld)\n", resu_k, resu_a, resu_b);
		else if (0 == resu_k && resu_a > 0)
			printf("%lld/%lld\n", resu_a, resu_b);
		else if (0 == resu_k && resu_a < 0)
			printf("(%lld/%lld)\n", resu_a, llabs(resu_b));
		else
			printf("%lld %lld/%lld\n", resu_k, resu_a, resu_b);
	}
}
void multiplication(long long int a1, long long int b1, long long int a2, long long int b2) {
	long long int resu_k, resu_a, resu_b, k1, k2;
	char ch = '*';
	if (0 == a1 || 0 == a2)//积
	{
		resu_a = 0;
		resu_k = 0;
	}
	else
	{
		resu_a = a1 * a2;
		resu_b = b1 * b2;
		yue_fen(&resu_a, &resu_b, &resu_k);
	}
	yue_fen(&a1, &b1, &k1);
	yue_fen(&a2, &b2, &k2);//分子分母有理化
	if (0 == a1)								//判断第一个有理数
	{
		if (k1 < 0)
			printf("(%lld)", k1);
		else
			printf("%lld", k1);
	}
	else
	{
		if (0 == k1)
		{
			if (a1 > 0)
				printf("%lld/%lld", a1, b1);
			else
				printf("(%lld/%lld)", a1, b1);
		}
		else if (k1 < 0)
			printf("(%lld %lld/%lld)", k1, a1, b1);
		else
			printf("%lld %lld/%lld", k1, a1, b1);
	}
	printf(" %c ", ch);
	if (0 == a2)								//判断第二个有理数
	{
		if (k2 < 0)
			printf("(%lld)", k2);
		else
			printf("%lld", k2);
	}
	else
	{
		if (0 == k2)
		{
			if (a2 > 0)
				printf("%lld/%lld", a2, b2);
			else
				printf("(%lld/%lld)", a2, b2);
		}
		else if (k2 < 0)
			printf("(%lld %lld/%lld)", k2, a2, b2);
		else
			printf("%lld %lld/%lld", k2, a2, b2);
	}
	printf(" = ");
	if (0 == resu_a)								//判断结果
	{
		if (resu_k < 0)
			printf("(%lld)\n", resu_k);
		else
			printf("%lld\n", resu_k);
	}
	else
	{
		if (resu_k < 0)
			printf("(%lld %lld/%lld)\n", resu_k, resu_a, resu_b);
		else if (0 == resu_k && resu_a > 0)
			printf("%lld/%lld\n", resu_a, resu_b);
		else if (0 == resu_k && resu_a < 0)
			printf("(%lld/%lld)\n", resu_a, llabs(resu_b));
		else
			printf("%lld %lld/%lld\n", resu_k, resu_a, resu_b);
	}
}
void division(long long int a1, long long int b1, long long int a2, long long int b2) {
	long long int resu_k, resu_a, resu_b, k1, k2;
	int mark = 0;
	char ch = '/';
	if (0 == a1 || 0 == a2)
	{
		mark = 1;
	}
	else if (a1 < 0 && a2 >0 || (a2 < 0 && a1 > 0))
	{
		mark = 0;
		resu_a = -1 * llabs(a1) * llabs(b2);
		resu_b = llabs(a2) * llabs(b1);
		yue_fen(&resu_a, &resu_b, &resu_k);
	}
	else
	{
		mark = 0;
		resu_a = -1 * a1 * b2;
		resu_b = -1 * a2 * b1;
		yue_fen(&resu_a, &resu_b, &resu_k);
	}
	yue_fen(&a1, &b1, &k1);
	yue_fen(&a2, &b2, &k2);//分子分母有理化
	{
		if (0 == a1)								//判断第一个有理数
		{
			if (k1 < 0)
				printf("(%lld)", k1);
			else
				printf("%lld", k1);
		}
		else
		{
			if (0 == k1)
			{
				if (a1 > 0)
					printf("%lld/%lld", a1, b1);
				else
					printf("(%lld/%lld)", a1, b1);
			}
			else if (k1 < 0)
				printf("(%lld %lld/%lld)", k1, a1, b1);
			else
				printf("%lld %lld/%lld", k1, a1, b1);
		}
		printf(" %c ", ch);
		if (0 == a2)								//判断第二个有理数
		{
			if (k2 < 0)
				printf("(%lld)", k2);
			else
				printf("%lld", k2);
		}
		else
		{
			if (0 == k2)
			{
				if (a2 > 0)
					printf("%lld/%lld", a2, b2);
				else
					printf("(%lld/%lld)", a2, b2);
			}
			else if (k2 < 0)
				printf("(%lld %lld/%lld)", k2, a2, b2);
			else
				printf("%lld %lld/%lld", k2, a2, b2);
		}
		printf(" = ");

		if (1 == mark)
		{
			printf("Inf\n");
		}
		else if (0 == resu_a)								//判断结果
		{
			if (resu_k < 0)
				printf("(%lld)\n", resu_k);
			else
				printf("%lld\n", resu_k);
		}
		else
		{
			if (resu_k < 0)
				printf("(%lld %lld/%lld)\n", resu_k, resu_a, resu_b);
			else if (0 == resu_k && resu_a > 0)
				printf("%lld/%lld\n", resu_a, resu_b);
			else if (0 == resu_k && resu_a < 0)
				printf("(%lld/%lld)\n", resu_a, llabs(resu_b));
			else
				printf("%lld %lld/%lld\n", resu_k, resu_a, resu_b);
		}
	}

}
int main()
{
	long long int a1, b1, a2, b2;
	long long int resu_k[4] = {}, resu_a[4] = {}, resu_b[4] = {};
	printf("请输入2个有理数：（形如2/3 -4/2）\n");
	scanf_s("%lld/%lld %lld/%lld", &a1, &b1, &a2, &b2);
	sum(a1, b1, a2, b2);
	subtraction(a1, b1, a2, b2);
	multiplication(a1, b1, a2, b2);
	division(a1, b1, a2, b2);
	return 0;
}