/*
(1) ���̺��͵ȼۣ�����P��Q = ?P��Q��P?Q =��P��Q���ţ�?P��?Q���ȼ۹�ϵ��ȥ�̺�����������˫��������?��
(2)�����ƣ�����??P = P��?��P��Q��= ?P��? Q��?��P��Q��= ?P��? Q��? (?x)P = (?x)(?P) ��?(?x)P = (?x)(?P)�ȼ۹�ϵ�ѷ񶨷��š�?���Ƶ�����ν��λ����
(3)������׼���� ����(?x)P��x��= (?y)P��y����(?x)P��x��= (?y)P��y���ȼ۹�ϵ��������׼������ʹÿ�����ʲ��ò�ͬ�ı���
(4)��ȥ��������?������������ʲ����κ�һ��ȫ�����ʵ�Ͻ���ڣ���ô������ʲ��������κ������ı�������˿���һ���µĸ��峣������ 
�罫(?x)P��x����ΪP(A)���������������ȫ�����ʵ�Ͻ���ڣ����ڹ�ʽ(��?y)��(?x)P��x��y�����У�����x��ȡֵ�����ڱ���y��ȡֵ��
��Skolem������f(y)����ʾ������ϵ ע�⣬������Ӧ��ԭ��ʽ��ʽ��û�еġ�
(5)����ʽ��Ϊǰ���Σ�������ȫ�������Ƶ���ʽ����ߣ���ʹÿ�����ʵ�Ͻ�����������ʺ�����������֣����õĹ�ʽ��Ϊǰ����
(6)��Ϊ��ȡ��ʽ:����P�ţ�Q��R��=��P��Q���ģ�P��R������P��Q���ţ�P��R��= P�ģ�Q��R���ȼ۹�ϵ��ĸʽ��Ϊ��ȡ��ʽ���Ӿ�ĺ�ȡʽ��
(7)��ȥȫ�����ʣ�ĸʽ�еı�������ȫ�����������ı���
(8)��ȥ��ȡ���šģ���ĸʽ���Ӿ伯��ʾ���磺P��Q�ɱ�ʾΪ���Ӿ伯�� P Q
(9)�Ӿ������׼������������������ʹÿ���Ӿ��еı������Ų�ͬ

(?x){[?P(x)��?Q(x)]��(?y)[S(x,y)��Q(x)]��(?x)[P(x)��B(x)]}

(1)(?x){?[?P��x����?Q(x)]��(? y)[S(x��y)��Q(x)]}��(?x)[P��x����B��x��]
(2)(?x){[P��x����Q(x)]��(? y)[S(x��y)��Q(x)]}��(?x)[P��x����B��x��]
(3)(?x){[P��x����Q(x)]��(? y)[S(x��y)��Q(x)]}��(?w)[P��w����B��w��]
(4)(?x)��{[P��x����Q(x )]��[S(x��f (x) ) ��Q(x )]}��(? w)[ P��w����B��w��]��
(5)(?x)(?w){[P��x����Q(x)]��[S(x��f(x))��Q(x)]}��[P��w����B��w��]
(6) (?x)(?w){[P��x����S(x��f(x))]��Q(x)��[P��w����B��w��]}
(7) [P��x����S(x��f(x))]��Q(x)��[P��w����B��w��]
(8) �Ӿ伯Ϊ�� P��x����S(x��f(x)����Q(x)��P��w����B��w��
(9) �Ӿ������׼�������յ��Ӿ伯Ϊ��
P��x����S��x��f(x)����Q��y����P��w����B��w��

*/

/*
��ʽ�淶��
1.���ʺ���ȸ����ű��������÷�Χ
2.���в�ͬ����֮�����������ȷ�����ȼ�
3.�����ڲ����������ǵ�����ĸ�Ұ��ֵ�������
4.��ʱ�������ڹ��ڸ��ӵľ��ӣ�Ʃ��������ർ��26����ĸ�����õ����
5.���Ҫ���й�ᣬȫ��ʹ�õ�����д��ĸ�ļ��ϱ�ʾ������ԭ��ʹ�õĴ�д��ĸ�䲻�ܳ�ͻ
*/

#include<iostream>
#include<io.h>
#include<fcntl.h>
#include"convertTree.h"
#include"convertClause.h"

using namespace std;
//(?x){{[?P(x)��?Q(x)]��(?y)[S(x,y)��Q(x)]}��(?x)[P(x)��B(x)]}
//(?(?x)(R(x)))��(?x)(?y)(?P(x,y)��?Q(x))
//A?B
//(P��Q)��(P��R)
//p��(q��p)
//P��((P��Q)��?(?Q��?P))
//((P��Q)��((P��R)��(Q��S)))��(S��R)
/*
?	@
?	#
?	$
��	-
?	!
��	*
��	+
*/
bool* exisUsed;
//(A+B)*(C+D+E)*B*C*(B+C+(A*D)+F)
//P��(Q��R)

void generate_clause(LogicNode*& root, char* u, int len, bool conclude = false);

void generate_clause(LogicNode*& root,char* u,int len,bool conclude)
{
	for (int i = 0; i < 26; i++)
	{
		clauseVariUsed[i] = 0;
		reflect[i] = { 0 };
	}
	first_del_arrow(root);
	wcout << L" (1) ���̺��͵ȼۣ�" << endl;
	showTree(root);
	second_del_neg(root);
	wcout << L"(2)�����ƣ�" << endl;
	showTree(root);
	third_var_regulation(root);
	wcout << L"(3)������׼����" << endl;
	showTree(root);
	char base[TEXTLEN] = { 0 };
	char exist[TEXTLEN] = { 0 };
	fourth_del_exist(root, base, 0, exist, 0,exisUsed);
	wcout << L"(4)��ȥ�������ʣ�" << endl;
	showTree(root);
	fifth_mov_all(root, root);
	wcout << L"(5)����ʽ��Ϊǰ���Σ�" << endl;
	showTree(root);
	root = collectUsefulNodes(root);
	//cout << "...." << endl;
	//showTree(root);
	adjustTree(root);
	wcout << L"(5.5)������ʽ:" << endl;
	showTree(root);
	sixth_convert_cnf(root);
	wcout << L"(6)��Ϊ��ȡ��ʽ:" << endl;
	showTree(root);
	int status=mergeRoot(root,conclude);
	wcout << L"(6.5)����" << endl;
	if (status == isNull)
	{
		wcout << L"null" << endl;
		if (conclude)
			wcout << L"���ۣ�����ķ񶨹������Ӿ䣬ԭ���������" << endl;
		else
			wcout << L"ǰ��������Ӿ䣬ǰ�᲻������" << endl;
		return;
	}
	showTree(root);
	seventh_del_all(root);
	wcout << L"(7)��ȥȫ�����ʣ�" << endl;
	showTree(root);
	wcout << L"(8)��ȥ��ȡ���ţ�" << endl;
	showTree(root, true);
	ninth_clause_var_regu(root,u,len);
	wcout << L"(9)�Ӿ������׼����" << endl;
	int t=showTree(root, true);
	if (conclude)
	{
		if (!t)
			wcout << L"���ۣ�����ķ񶨹������Ӿ䣬ԭ���������" << endl;
		else
			wcout << L"���ۣ�����ķ񶨹����ǿ��Ӿ䣬ԭ���ⲻ������" << endl;
	}
}

//(#x)(pass(x)-happy(x))*(#y)((learn(y)+lucky(y))-(pass(y)))*(!(learn(A)))*lucky(A)*(#t)(lucky(t)-win(t))
//(#x)(#y)(murder(x,y)-hate(x,y))*(#m)(hate(A,m)-!hate(C,m))*(#n)(!isB(n)-hate(A,n))*!isB(A)*!isB(C)*isB(B)*(#t)(lessWealthy(t,A)-hate(B,t))*(#s)(hate(A,s)-hate(B,s))*!(@p)(#q)(hate(p,q))*(#j)(#k)(murder(j,k)-lessWealthy(j,k))*(@e)(murder(e,A))

int main()
{
	_setmode(_fileno(stdout), _O_U16TEXT);
	_setmode(_fileno(stdin), _O_U16TEXT);
	wchar_t a[1000] = { 0 };
	char str[1000] = { 0 };
	wchar_t wu[30] = { 0 };
	char u[30] = { 0 };
	int uLen = 0;
	exisUsed=new bool[26];
	for (int i = 0; i < 26; i++)
		exisUsed[i] = 0;
	wcout << L"������Ԫ��ȫ������д��ĸ��:"<<endl;
	wcout << L"**ע�⣺������Ǵ�д��ĸ����ֻ�ɽ��������߼���ᣬ���ɽ���һ���߼����**" << endl;
	wcin >> wu;

	for (int i = 0; i < 30; i++)
	{
		u[i] = (char)wu[i];
		if (isUpper(u[i]))
		{
			exisUsed[u[i] - 'A'] = true;
		}
	}
	while (u[uLen])
		uLen++;
	if (!isUpper(u[0]))
		uLen = 0;
	wcout << L"������ǰ�᣺" << endl;
	wcin >> a;
	int len= formRead(a, str);
	wcout << L">>>>>��Ϊ�Ӿ�<<<<<" << endl;
	LogicNode* root=strToTree(str,len);
	generate_clause(root,u,uLen);
	wcout << L">>>>>��ʼ���<<<<<" << endl;
	//if (uLen)
	wcout << L"����������ʣ�" << endl;
	deal_exist(root, u, uLen);
	int ori=showTree(root);
	if (!ori)
	{
		wcout << L"ǰ����Ϊ���Ӿ䣬��������" << endl;
		deleteTree(root);
		system("pause");
		return 0;
	}
	wchar_t b[1000] = { 0 };
	char bStr[1000] = { 0 };
	//LogicNode* concludeRoot=copyTree(root);//ʼ����ǰ�������root����һ�£��ɶ��֤������
	LogicNode* proNode, * addPos,*nRoot;//proNode����Ҫ֤�����������γɵĽڵ㣬addPos��proNodeӦ�����λ�õ�ǰ��
	wcout << L"��������������ٵ����⣺" << endl;
	for (int i = 0; i < 1000; i++)
		b[i] = 0;
	wcin >> b;
	int bLen = formRead(b, bStr, exisUsed);
	proNode = strToTree(bStr, bLen);
	if (!proNode)
		return 0;
	proNode->antiFlag = true;
	proNode->emptyFlag = false;
	addPos = root->child;
	if (!addPos || addPos->broLink == '+')
	{
		nRoot = new LogicNode;
		nRoot->child = root;
		root->broLink = '*';
		root->brother = proNode;
		root = nRoot;
	}
	else
	{
		while (addPos->brother)
			addPos = addPos->brother;
		addPos->broLink = '*';
		addPos->brother = proNode;
	}
	wcout << L"��0��������ķ񶨼���ǰ���Ӿ伯��" << endl;
	showTree(root);
	generate_clause(root, u, uLen, true);
	deleteTree(root);
	//deleteTree(concludeRoot);
	delete[]exisUsed;
	system("pause");
	return 0;
	system("pause");
	return 0;
}


/*
(  (  ((  (A*!B)  +  (!A*B)  ))  +  C  )  *  (  ((  (!A+B)  *  (A+!B)  ))  +  !C  )  )
(A?B)?C
*/
