from test import Checker

c = Checker()
c.dump_result()

######################################

c.check("int main() { char a; return sizeof +a; }" , 4)
c.check("int main() { char a; return sizeof((a+a)); }", 4)
c.check("int main() { char a; return sizeof(a+a); }" , 4)

c.check('int main(void){int a[5]; a[1] = 174; int *p = a + 3; p -= 2; return *p;}' , 174)
c.check('int main(void){char a[5]; a[1] = 74; char *p = a + 3; p -= 2; return *p;}' , 74)
c.check('int main(void){int a[5]; a[3] = 174; int *p = a + 2; p++; return *p;}' , 174)
c.check('int main(void){int a[5]; a[3] = 174; int *p = a + 3; return *p++;}' , 174)

c.check('int main(){return sizeof(int);}' , 4)
c.check('int main(){return sizeof(int*);}' , 8)
c.check('struct A{int a; int b;}; int main(){ return sizeof(struct A);}' , 8)
c.check('struct A{int a; char c; char d; int b;}; int main(){ return sizeof(struct A);}' , 12)

c.check('int *f(int *p){return p;} int main(){int a[4]; a[0] = 1; f(a)[0]++; f(a)[1] = 172; return a[1]+a[0];}', 174)
c.check('struct A{char a; int b;}; int main(){struct A a; a.a = 74; return a.a;}' , 74)
c.check('struct A{int a; int b;}; int main(){struct A a; a.a = 174; return a.a;}' , 174)
c.check('struct A{int a; int b;}; int main(){struct A a; a.a = 174; return a.a;}' , 174)
c.check('int main(){int a; int *p; p = &a; *p = 2; int *q; q = &*p; *q = 174; return a;}' , 174)
c.check('int main(){int a; int *p; p = &a; *p = 2; int *q; q = &(*p); *q = 174; return a;}' , 174)
c.check('char foo(char *p){char a; return a;} int main(){char q; foo(&(q)); return 174;}' , 174)

c.check('int main(){/**/return 123;}' , 123)
c.check('int main(){/*u89g3wihu-@w3erolk*/ return (123);}' , 123)
c.check('int/*/* 0^[o;:._/-*/main(){return ((((123))));}' , 123)
c.check('int main(){int a[10]; a[5] = 173; int b; b = a[5]++; return a[5]*!(a[5]-b-1);}' , 174)
c.check('int main(){int a[1]; int *p; p = a; *p=2; return 174;}' , 174)
c.check('int main(){int a[1]; *(a+0)=2;return 174;}' , 174)
c.check('int x; int *y; int main(){x=3; int a[1]; *a=2; y=a; return x+*y+169;}' , 174)
c.check('int x; int main(){x=3; int *y; y=&x; return *y+171;}' , 174)
c.check('int a[1]; int main(){ *a=2;return 174;}' , 174)
c.check('int main(){int a[1][2];int *q;q = *a;return 174;}' , 174)
c.check('int main(){int a[1][2];int *q;q = *a; *q=174; return **a;}' , 174)
c.check('int main(){int a[86][2];int *q;q = *(a+1); *q=174; return **(a+1);}' , 174)
c.check('int main(){int a[5][6];int *q;q = *(a+1); *(2+q)=174; return *(*(1+a)+2);}' , 174)

c.check('int main(){int a[5][6];int *q;q = a[1]; 2[q]=174; return 1[a][2];}' , 174)
c.check('int main(){return 123;}' , 123)
c.check('int main(){return (123);}' , 123)
c.check('int main(){return ((((123))));}' , 123)
c.check('int main(){return 123+51;}' , 174)
c.check('int main(){return 123+56-5;}' , 174)
c.check('int main(){return 175-(4-3);}' , 174)
c.check('int main(){return 181-4-3;}' , 174)
c.check('int main(){return 6*(3+7)-5*1;}' , 55)

c.check('int main(){return +174;}' , 174)
c.check('int main(){return -(1-175);}' , 174)
c.check('int main(){23; 45+37; ((12-1)*75); return -(1-175);}' , 174)
c.check('int main(){23; 45+37; return -(1-175); ((12-1)*75);}' , 174)

c.check('int add_(int x, int y){4; return x+y;} int main(){3; return add_(87,87);}' , 174)
c.check('int main() { return (3 && 2 && 5) + 173; }' , 174)
c.check('int main() { return (3 && 2) + !(3 && 0) + !(0 && 3)+ !(0 && 0) + 170; }' , 174)
c.check('int main() { return (3 || 2 || 5) + 173; }' , 174)
c.check('int main() { return (3 || 2) + (3 || 0) + (0 || 3)+ !(0 || 0) + 170; }' , 174)
c.check('int main() {int a; a = 3; a += 5;  return a + 166; }' , 174)
c.check('int main() {int a; int b; a = 3; b = (a += 5);  return a + b + 158; }' , 174)
c.check('int main() {int a; int b; a = 3; b = 1; b *= (a += 5);  return a + b + 158; }' , 174)
c.check('int main() {int a; int b; a = 11; a -=5; a /= 2; b = 1; b *= (a += 5);  return a + b + 158; }' , 174)
c.check('int foo(){ return 2;} int main() {int a; int b; int c; a = 3;b = 5;c = 2;if(a) {b = foo();} else { }    return 172+b;}' , 174)
c.check('int foo(){ return 2;} int main() {int a; int b; int c; a = 3;b = 5;c = 2;if(a) {b = foo();}   return 172+b;}' , 174)
c.check('int foo(){ return 2;} int bar(){ return 7;} int main() {int a; int b; int c; a = 3;b = 5;c = 2;if(a) {b = foo();} else { c = bar();}    return 172+b;}' , 174)
c.check('int foo(){ return 2;} int bar(){ return 7;} int main() {int a; int b; int c; a = 0;b = 5;c = 2;if(a) {b = foo();} else { c = bar();}    return 162+b+c;}' , 174)
c.check('int foo(){ return 2;} int bar(){ return 7;} int main() {int a; int b; int c; a = 3;b = 5;c = 2;if(a) if(0) { b = foo(); } else {  c = bar(); }    return 162+b+c;}' , 174)
c.check('int foo(){ return 2;} int bar(){ return 7;} int main() {int a; int b; int c; a = 3;b = 5;c = 2;if(a) if(0)b=foo();else c = bar();return 162+b+c;}' , 174)
c.check('int main() {int a; a = 4; if(1){return 170+a; a = 7; }else{return 170-a; a = 9;} a = 5; return a;}' , 174)
c.check('int foo(){return 3;} int main() {int a; a = 0;while(a == foo()) {a = 3;}return 174;}' , 174)
c.check('int main(){int a; int b; a = 0; b = 0; while(a <= 10) {b += a; a += 1;}return b;}' , 55)
c.check('int main(){int a; int b; a =-3; b=-6; return a*b*10+a+b+3;}' , 174)
c.check('int main(){int a; int b; a=3; b=0; b+= a++; return !(b-3)+!(a-4)+172;}' , 174)

c.check('struct A {int a;};int main(){const struct A *a; return 174;}' , 174)
c.check('int main(void){int a = 5; return 174;}' , 174)
c.check('int main(void){int u = 0; for(int a = 0; a < 10; a++){ u += a; } return 174+u-45;}' , 174)
c.check('int main(void){int a = 5; int *p = &a; return 174;}' , 174)
c.check('int main(void){int a = 4; int *p = &a; *p += 170; return a;}' , 174)
c.check('int main(){int a; int *p = &a; *p = 2; int *q = &*p; *q = 174; return a;}' , 174)
c.check('int main(){int a; int *p = &a; *p = 2; int *q = &(*p); *q = 174; return a;}' , 174)
c.check('int main(){int x = 86;int *y = &x; return (*y) + x + 2;}' , 174)
c.check('int main(){int x = 86;int *y = &x; return (*y) + (*y) + 2;}' , 174)
c.check('int main(){int x = 86;int *y = &x;int **z = &y;return (*y) + (**z) + 2;}' , 174)
c.check('int main(){int x = 86;int *y = &x;int **z = &y;return*y+**z+2;}' , 174)

c.check('struct A{int a; int b;}; int main(){ struct A a; return 174;}' , 174)
c.check('struct A{int a; int b;}; int main(){ struct A a[10]; return 174;}' , 174)
c.check('struct A{int a; int b;};  struct A a[10]; int main(){return 174;}' , 174)
c.check('int printf();int a() {return 3;}int main() {int i; printf("%d %d", i, a()); return 0;}' , 0)
c.check('int foo(char *a, int b, int c){return 0;} int a(int N) {return 3;}int main() {int i; foo("%d %d", i, a(i)); return 0;}' , 0)
c.check('int printf();int a(int N) {return 3;}int main() {int i; printf("%d %d", i, a(i)); return 0;}' , 0)
c.check('int printf();int puts();int a(int N) {return 3;}int main() {int i; for (i = 1; i <= 12; i++) { printf("%d %d", i, a(i)); puts("");} return 0;}' , 0)
c.check('int printf();int puts();int A[200][200];int a(int row, int N) {return 3;}int main() {int i; for (i = 1; i <= 12; i++) { printf("%d %d", i, a(0, i)); puts("");} return 0;}' , 0)
c.check('int printf();int puts();int A[200][200];int dfs(int row, int N) { if (row == N) return 1; int ret;ret = 0; int col;for (col = 0; col < N; col++) { int ok; ok = 1; int i; for (i = 1; i < N; i++) { if (row - i >= 0 && col - i >= 0) { ok = ok && A[row - i][col - i] == 0; } if (row - i >= 0) { ok = ok && A[row - i][col] == 0; } if (row - i >= 0 && col + i < N) { ok = ok && A[row - i][col + i] == 0; } } if (ok) { A[row][col] = 1; ret += dfs(row + 1, N); A[row][col] = 0; } } return ret;}int main() {int i; for (i = 1; i < 12; i++) { printf("%d queen: %d", i, dfs(0, i)); puts("");} return 0;}' , 0)
c.check('char foo(){char a; return a;} int main(){foo(); return 174;}' , 174)
c.check('char foo(char *p){char a; return a;} int main(){char q; foo(&q); return 174;}' , 174)
c.check('char foo(char *p){char a; a = 5; return a;} int main(){char q; foo(&q); return 174;}' , 174)
c.check('int main(){char x[3]; x[0] = -1; x[1] = 2; int y; y = 4; return x[0] + y + 171;}' , 174)
c.check('char foo(char *p){*p = 5; char a;a = 3; return a;} int main(){char q; char r; r = foo(&q); return 172-r+q;}' , 174)
c.check('char a;char foo(char *p){*p = 5; a = 3; return a;} int main(){char q; char r; r = foo(&q); return 172-r+q;}' , 174)
c.check('int foo(char a){int d;d = 3;char c;c = a+d;return c;} int main(){char f;f=3;return foo(f)*4+150;}' , 174)
c.check('int foo(char a){int d;d = 3;char c;c = a+d;return c*4;} int main(){char f;f=3;return foo(f)+150;}' , 174)
c.check('int foo(char a, char b){return 23;} int main(){char f;f=3;return foo(f,4)+151;}' , 174)
c.check('int foo(char a, char b){return a*4+11;} int main(){char f;f=3;return foo(f,4)+151;}' , 174)
c.check('int foo(char a, char b){return a*4+12;} int main(){char f;f=3;return foo(f,4)+150;}' , 174)
c.check('int foo(char a, char b){return (a+3)*4;} int main(){char f;f=3;return foo(f,4)+150;}' , 174)
c.check('int foo(char a, char b){char c;c = a+3;return c*4;} int main(){char f;f=3;return foo(f,4)+150;}' , 174)
c.check('int foo(char a, char b){int d;d = 3;char c;c = a+d;return c*4;} int main(){char f;f=3;return foo(f,4)+150;}' , 174)
c.check('int foo(char a, char b){int d;d = 3;char c;c = a+d;return c*b;} int main(){char f;f=3;return foo(f,4)+150;}' , 174)
c.check('char foo() { char *x;x = "1ab"; return x[0]; }int main(){ char *y;y = "a2b"; int z;z = 12; char a;a = y[1]; return (a-foo())*z+162;}' , 174)
c.check('int printf();int main(){printf("%d %s", 1, "a");return 174;}' , 174)
c.check('int printf();int puts();int A[200][200];int main() {int i; for (i = 1; i <= 12; i++) { printf("%d %d", i, i); puts(""); } return 0;}' , 0)
c.check('int printf();int puts();int a(int b, int c) {return 3;}int main() {int i; for (i = 1; i <= 12; i++) { int j;j = a(0, i); printf("%d %d", i, j); puts("");} return 0;}' , 0)
c.check('int printf();int puts();int A[200][200];int dfs(int row, int N) { if (row == N) return 1; int ret;ret = 0; int col;for (col = 0; col < N; col++) { int ok; ok = 1; int i; for (i = 1; i < N; i++) { if (row - i >= 0 && col - i >= 0) { ok = ok && A[row - i][col - i] == 0; } if (row - i >= 0) { ok = ok && A[row - i][col] == 0; } if (row - i >= 0 && col + i < N) { ok = ok && A[row - i][col + i] == 0; } } if (ok) { A[row][col] = 1; ret += dfs(row + 1, N); A[row][col] = 0; } } return ret;}int main() {int i; for (i = 1; i < 11; i++) { int j; j = dfs(0, i); printf("%d queen: %d", i, j); puts("");} return 0;}' , 0)

c.check('int *foo(){return 0;} int main(){int *p = foo(); if (p == 0) {return 174;} else {return 1;} }' , 174)
c.check('int main(){int a[5];int *p = a;if (p == 0) {return 174;} else {return 1;}}' , 1)
c.check('int main(){int a[5];int *p = 0;if (p == 0) {return 174;} else {return 1;}}' , 174)
c.check('int main(){int a[5];int *p = 0;if (p != 0) {return 174;} else {return 1;}}' , 1)
c.check('int main(){int a[5];int *p = a;if (p != 0) {return 174;} else {return 1;}}' , 174)
c.check('int main(); int main(void){return 174;} int main(void);' , 174)
c.check('int main(){int a[5];int *p = a;int *q = a+3;if (p < q) {return 174;} else {return 1;}}' , 174)
c.check('int main(){int a[5];int *p = a;int *q = a+3;if (p > q) {return 174;} else {return 1;}}' , 1)
c.check('int main(){int a[5];int *p = a;int *q = a+3;if (p <= q) {return 174;} else {return 1;}}' , 174)
c.check('int main(){int a[5];int *p = a;int *q = a+3;if (p >= q) {return 174;} else {return 1;}}' , 1)
c.check('int main(){int a[5];int *p = a;int *q = a;if (p < q) {return 174;} else {return 1;}}' , 1)
c.check('int main(){int a[5];int *p = a;int *q = a;if (p > q) {return 174;} else {return 1;}}' , 1)
c.check('int main(){int a[5];int *p = a;int *q = a;if (p <= q) {return 174;} else {return 1;}}' , 174)
c.check('int main(){int a[5];int *p = a;int *q = a;if (p >= q) {return 174;} else {return 1;}}' , 174)
c.check('int main(){int a[5];int *p = a;int *q = a;if (p == q) {return 174;} else {return 1;}}' , 174)
c.check('int main(){int a[5];int *p = a;int *q = a;if (p != q) {return 174;} else {return 1;}}' , 1)
c.check('int main(){int a[5];int *p = a;int *q = a+3;if (p == q) {return 174;} else {return 1;}}' , 1)
c.check('int main(){int a[5];int *p = a;int *q = a+3;if (p != q) {return 174;} else {return 1;}}' , 174)
c.check('int main(void){int a[5]; a[3] = 174; int *p = a; p += 3; return *p;}' , 174)

c.check('int main(void) {char a = 74; char *p = &a; return *p+100;} ' , 174)
c.check('struct A{char a; int b;}; int main(){struct A a; a.a = 74; struct A b; b = a; return b.a;}' , 74)
c.check('struct A{char a; int b;}; int main(){struct A a; a.a = 74; struct A b = a; return b.a;}' , 74)
c.check('struct A{int a; int b;}; int main(){struct A a; a.a = 174; struct A b = a; return b.a;}' , 174)
c.check('struct A{int a; int b;}; int main(){struct A a; a.a = 174; struct A b = a; return b.a;}' , 174)

c.check('struct A{int a;}; int main(){struct A arr[5]; void *p = arr; int *q = p; q[3] = 174; return arr[3].a;}' , 174)
c.check('int main(){int a[5]; if(a){return 174;} return 0;}' , 174)
c.check('int main(void){int p = 0; return (!p)*174; }' , 174)
c.check('int main(void){int *p = 0; return (!p)*174; }' , 174)
c.check('int main(void){int q; int *p = &q; return (1+!p)*174;}' , 174)
c.check('struct A{int a;}; struct A f(void) {struct A u; u.a = 174; return u;} int main(void){struct A u = f(); return u.a;}' , 174)

c.check('void f(int *p){*p = 174;} int main(void){ int a; f(&a); return a;}' , 174)
c.check('int main(){int *p; p = 0; if(p) {return 4; } return 174;}' , 174)
c.check('int main(){int *p; int a; p = &a; if(p) {return 4; } return 174;}' , 4)
c.check('int main(){int *p; int a; p = &a; return p && &p;}' , 1)
c.check('int main(){int *p; int a; p = &a; return p || &p;}' , 1)
c.check('int main(void){return 174;}' , 174)
c.check('int main(void){void *p; p = 0; p = p; return 174;}' , 174)
c.check('struct A{int a; int b;}; int main(){ struct A *p; void *q1; void *q2; q1 = p; q2 = p+1; char *r1; char *r2; r1 = q1; r2 = q2; return r2-r1;}' , 8)
c.check('void f(int *p){*p = 174; return;} int main(void){ int a; f(&a); return a;}' , 174)
c.check('int main(){int a; a = 3; { a = 174;} return a;}' , 174)
c.check('int main() {int *b; int a; a = 3; a += 5;  return a + 166; }' , 174)
c.check('int main() {int *******b; int a; a = 3; a += 5;  return a + 166; }' , 174)
c.check('int main() {int a; a = 174; int *b; b = &a; return a;}' , 174)
c.check('int main(){int x;x = 86;int *y;y = &x; return (*y) + x + 2;}' , 174)
c.check('int main(){int x;x = 86;int *y;y = &x; return (*y) + (*y) + 2;}' , 174)
c.check('int main(){int x;x = 86;int *y;y = &x;int **z;z = &y;return (*y) + (**z) + 2;}' , 174)
c.check('int main(){int x;x = 86;int *y;y = &x;int **z;z = &y;return*y+**z+2;}' , 174)
c.check('int main() {int x;int *y;x = 3;y = &x;*y = 174;return x;}' , 174)
c.check('int main() {int x;int *y;x = 3;y = &x;*y = 171;*y += 3;return x;}' , 174)
c.check('int main(){int x; int y; int *z; int*a; z=&x; a=&y; *z=*a=87; return(x+y);}' , 174)
c.check('int main(){int x; int *y; int **z; z = &y; *z = &x; *y = 174; return x;}' , 174)
c.check('int foo(int* p){return 3;} int main(){int x; return 174;}' , 174)
c.check('int foo(int* p){return *p;} int main(){int x; x = 174; return foo(&x);}' , 174)
c.check('int foo(int* p){*p = 172; return *p+2;} int main(){int x; return foo(&x);}' , 174)
c.check('int *foo(int *p){*p = 4;return p;} int main(){int x;int *y;y = foo(&x); *y+= 170;return x;}' , 174)
c.check('int *foo(int *p){*p = 4;return p;} int main(){int x;int y;*foo(&x) += 170;return x;}' , 174)
c.check('int *foo(int *p){*p = 4;return p;} int main(){int x;int y; int **z; *foo(&x) += 170;return x;}' , 174)
c.check('int main(){int a[2][3]; return 174;}' , 174)
c.check('int x; int *y; int main(){return 174;}' , 174)
c.check('int x; int *y; int main(){return x+174;}' , 174)
c.check('int x; int *y; int main(){x=3; int a; a=2; y=&a; return x+*y+169;}' , 174)

c.check('struct A {int k[15];}; int main(){struct A s; s.k[3] = 35; return s.k[3];}' , 35)
c.check('struct A {int a; int b; int c;}; int main(){struct A a[5]; return a + 3 - a;}' , 3)
c.check('struct A {int k[15];}; int main(){struct A a[5]; return a + 3 - a;}' , 3)

c.check('int main(){char a[456]; return a + 3 - a; }' , 3)
c.check('struct A {int k[15];}; int main(){struct A s; return 3;}' , 3)
c.check('struct A {int k[15]; int a;}; int main(){struct A s; s.a = 3; return s.a;}' , 3)
c.check('struct A {int k[15]; int a;}; int main(){return sizeof(struct A);}' , 64)
c.check('struct A {int k[15];}; int main(){struct A s; void *p = s.k; return 35;}' , 35)
c.check('struct A {int k[15];}; int main(){struct A s; int *p = s.k; return 35;}' , 35)

c.check('int main() {return 0;} //nfsjdgkssfdvc' , 0)
c.check('int main() { int *a; return sizeof a; }' , 8)
c.check('int main() { int *a; return sizeof (a+0); }' , 8)
c.check('int main() { int a[2][3]; return sizeof a; }' , 24)
c.check('int main() { int a[2][3]; return sizeof (a+0); }' , 8)
c.check('int main() { int a; return sizeof a; }' , 4)
c.check("int main() { return sizeof 'C'; }" , 4)
c.check("int main() { char a; return sizeof a; }" , 1)

c.check('int main() { int a; if (1) { a = 3; } else { a = 7; } return a; }' , 3)
c.check('void foo(int*p) {*p=3;} int main() { int a; if (0) { foo(&a); } else { a = 7; } return a; }' , 7)
c.check('void foo(int*p) {*p=7;} int main() { int a; if (0) { a = 3; } else { foo(&a); } return a; }' , 7)

c.check("""
int printf();
int first() {
    printf("first, ");
    return 0;
}
int second() {
    printf("second, ");
    return 0;
}
int main() { return first() || second(); }
""", 0, expected_stdout="first, second, ")

c.check("""
int printf();
int first() {
    printf("first, ");
    return 1;
}
int second() {
    printf("second, ");
    return 0;
}
int main() { return first() || second(); }
""", 1, expected_stdout="first, ")

c.check("""
int printf();

int main() {
    for (int i = 0 - 1; i >= 2; i--) {
        printf("%d", i);
    }
    return 0;
}
""", 0, expected_stdout="")

c.check("""
int printf();

int main() {
    for (int i = -7; i <= 2; i++) {
        printf("%d", i);
    }
    return 0;
}
""", 0, expected_stdout="-7-6-5-4-3-2-1012")

c.check(r'int foo(void); int foo() { return 3; } int main() { return foo(); }', 3)
c.check(r'int main(void) { return sizeof("\0173"); }', 3)

c.check(r'int main() { return sizeof("\0173"); }', 3)
c.check(r'int main() { return "\0173"[1]; }', 51)
c.check(r'int main() { return "\0173"[0]; }', 0o17)

c.check("""
struct Token {
    char kind;
    int value;
};

struct Token tokens[5];

int main(int argc, char **argv) {
    return sizeof(tokens);
}
""", 40)

c.check("""int printf();
int isDigit(char c) {
    return '0' <= c && c <= '9';
}
int parseInt(const char *str) {
    int result = 0;
    while (isDigit(*str)) {
        int digit = *str - '0';
        result = result * 10 + digit;
        str++;
    }
    return result;
}
int main() {
    return parseInt("42");
}""", 42)

c.check("""int printf();
int isDigit(char c) {
    return '0' <= c && c <= '9';
}
int parseInt(const char *str) {
    int result = 0;
    while (isDigit(*str)) {
        int digit = *str - '0';
        result = result * 10 + digit;
        str++;
    }
    return result;
}
int main() {
    printf("%d", parseInt("42")); 
    return 0;
}""", 0, expected_stdout="""42""")

c.check("""int printf();
int isDigit(char c);
void *calloc();
int parseInt(char *str) {
    int result = 0;
    while (isDigit(*str)) {
        int digit = *str - '0';
        result = result * 10 + digit;
        str++;
    }
    return result;
}
int intLength(char *str) {
    int length = 0;
    while (isDigit(*str)) {
        length++;
        str++;
    }
    return length;
}
int isDigit(char c) {
    return '0' <= c && c <= '9';
}
int main() {
    char *p = calloc(3, 1);
    p[0] = '0';
    p[1] = 0;
    printf(".intel_syntax noprefix\\n");
    printf(".globl main\\n");
    printf("main:\\n");
    int parsednum_ = parseInt(p);
    int parsedlength_ = intLength(p);
    p += parsedlength_;
    printf("  mov rax, %d\\n", parsednum_);
    while (*p) {
        if (*p == '+') {
            p++;
            int parsednum = parseInt(p);
            int parsedlength = intLength(p);
            p += parsedlength;
            printf("  add rax, %d\\n", parsednum);
        } else if (*p == '-') {
            p++;
            int parsednum2 = parseInt(p);
            int parsedlength2 = intLength(p);
            p += parsedlength2;
            printf("  sub rax, %d\\n", parsednum2);
        } else {
            return 2;
        }
    }
    printf("  ret\\n");
    return 0;
}""", 0, expected_stdout=""".intel_syntax noprefix
.globl main
main:
  mov rax, 0
  ret
""")

c.check("""
int isDigit(char c);
int parseInt(char *str) {
    int result = 0;
    while (isDigit(*str)) {
        int digit = *str - '0';
        result = result * 10 + digit;
        str++;
    }
    return result;
}
int intLength(char *str) {
    int length = 0;
    while (isDigit(*str)) {
        length++;
        str++;
    }
    return length;
}
int isDigit(char c) {
    return '0' <= c && c <= '9';
}
int main() { return parseInt("123"); }""", 123)

c.check("""
int isDigit(char c) {
    return '0' <= c && c <= '9';
}
int intLength(char *str) {
    int length = 0;
    while (isDigit(*str)) {
        length++;
        str++;
    }
    return length;
}
int main() { return intLength("012a"); }
""", 3)

c.check("""
int isDigit(char c) {
    return '0' <= c && c <= '9';
}
int main() { for(int a = ' '; a <= '~'; a++) { if (isDigit(a)) {printf("%c", a);} } return 0; }
""", 0, expected_stdout="0123456789")

c.check("void foo(int *p) { *p = 3; return; } int main() { int a; foo(&a); return a; }", 3)

c.check("""
int printf();
int enum2(int a, int b) {
    printf("a=%d, b=%d; ", a, b);
    return a + b * 10;
}

int enum3(int a, int b, int c) {
    printf("a=%d, b=%d, c=%d; ", a, b, c);
    return enum2(a, b + c * 10);
}

int main() {
    printf("res=%d", enum3(1, 2, 3));
    return 0;
}
""", expected=0, expected_stdout="a=1, b=2, c=3; a=1, b=32; res=321")

c.check("""
int printf();
int enum2(int a, int b) {
    return a + b * 10;
}

int enum3(int a, int b, int c) {
    return enum2(a, enum2(b, c));
}

int main() {
    printf("%d", enum3(1, 2, 3));
    return 0;
}
""", expected=0, expected_stdout="321")


c.check("""
void *calloc();
char *strncpy();
int printf();
char *decode_kind(int kind) {
    void *r = &kind;
    char *q = r;
    char *ans = calloc(5, sizeof(char));
    strncpy(ans, q, 4);
    return ans;
}

int enum2(int a, int b) {
    return a + b * 256;
}

int enum3(int a, int b, int c) {
    return enum2(a, enum2(b, c));
}

int enum4(int a, int b, int c, int d) {
    return enum2(a, enum3(b, c, d));
}

int main() {
    printf("%s", decode_kind(enum3('a', 'b', 'c')));
    return 0;
}
""", expected=0, expected_stdout="abc")

c.check("""
void *calloc();
char *strncpy();
int printf();
char *decode_kind(int kind) {
    void *r = &kind;
    char *q = r;
    char *ans = calloc(5, sizeof(char));
    strncpy(ans, q, 4);
    return ans;
}

int enum2(int a, int b) {
    return a + b * 256;
}

int enum3(int a, int b, int c) {
    return enum2(a, enum2(b, c));
}

int enum4(int a, int b, int c, int d) {
    return enum2(a, enum3(b, c, d));
}

int main() {
    printf("%s", decode_kind(enum4('v', 'o', 'i', 'd')));
    return 0;
}
""", expected=0, expected_stdout="void")

c.check("""
int printf();
int enum2(int a, int b) {
    printf("a=%d, b=%d; ", a, b);
    return a + b * 10;
}

int enum3(int a, int b, int c) {
    return enum2(a, b + c * 10);
}

int main() {
    printf("res=%d", enum3(1, 2, 3));
    return 0;
}
""", expected=0, expected_stdout="a=1, b=32; res=321")

c.check("int a; void foo(int *p) { *p = 3; return; } int main() { foo(&a); return a; }", 3)

c.check("""
void *calloc();
char *strncpy();
int printf();
char *decode_kind(int kind) {
    void *r = &kind;
    char *q = r;
    char *ans = calloc(5, sizeof(char));
    strncpy(ans, q, 4);
    return ans;
}

int enum2(int a, int b) {
    return a + b * 256;
}

int enum3(int a, int b, int c) {
    return enum2(a, enum2(b, c));
}

int enum4(int a, int b, int c, int d) {
    return enum2(a, enum3(b, c, d));
}

int main() {
    printf("%s", decode_kind('a'));
    return 0;
}
""", expected=0, expected_stdout="a")

c.check("""
void *calloc();
char *strncpy();
int printf();
char *decode_kind(int kind) {
    void *r = &kind;
    char *q = r;
    char *ans = calloc(5, sizeof(char));
    strncpy(ans, q, 4);
    return ans;
}

int enum2(int a, int b) {
    return a + b * 256;
}

int enum3(int a, int b, int c) {
    return enum2(a, enum2(b, c));
}

int enum4(int a, int b, int c, int d) {
    return enum2(a, enum3(b, c, d));
}

int main() {
    printf("%s", decode_kind(enum2('a', 'b')));
    return 0;
}
""", expected=0, expected_stdout="ab")

c.check("""
int bar(int *p, void *q) {
    return p == q;
}
int bar2(int *p, void *q) {
    p = q;
    q = p;
    return 0;
}
int main() { return 0; }
""", 0)

c.check_and_link_with(
    "struct A { int a; int b; }; int foo(); int main() { struct A s; foo(&s); return (&s)->b - (&s)->a; }",
    linked_lib="struct A { int a; int b; }; int foo(struct A *p) { p->a = 3; p->b = 24; return 0; }",
    expected=21)

c.check_and_link_with(
    "struct A { char a[5]; int b; }; int foo(); int main() { struct A s; foo(&s); return (&s)->a[2] + (&s)->b; }",
    linked_lib="""
struct A { char a[5]; int b; }; 
int foo(struct A *p) { 
    p->a[0] = 1; 
    p->a[1] = 3; 
    p->a[2] = 5; 
    p->a[3] = 7; 
    p->a[4] = 9; 
    p->b = 24; 
    return 0; 
}""",
    expected=5+24)

c.check_and_link_with(
    "struct A { char a[5]; int b; }; int foo(); int main() { struct A s; foo(&s); return s.a[2] + s.b; }",
    linked_lib="""
struct A { char a[5]; int b; }; 
int foo(struct A *p) { 
    p->a[0] = 1; 
    p->a[1] = 3; 
    p->a[2] = 5; 
    p->a[3] = 7; 
    p->a[4] = 9; 
    p->b = 24; 
    return 0; 
}""",
    expected=5+24)

c.check("struct A { int a; int b; }; int main() { return 0; }", 0)
c.check("struct A { int a; int b; }; int main() { return sizeof(struct A); }", 8)
c.check("struct A { char a; int b; }; int main() { return sizeof(struct A); }", 8)
c.check("struct A { char a[5]; int b; }; int main() { return sizeof(struct A); }", 12)

c.check("int main() { return sizeof(struct A*); }", 8)
c.check("int main() { struct A *p; return 0; }", 0)

c.check("int main() { return 1+(2!=1+1); }", 1)
c.check("int main() { return 5+(8+(7!=2)); }", 14)

# miscompiles

c.check("int main() { return 8*7!=2; }", 1)
c.check("int main() { return 8+7!=2; }", 1)
c.check("int main() { return 1+(1+1!=1+1); }", 1)
c.check("int main() { return 1+(1+1!=2); }", 1)
c.check("int main() { return 5+(8+7!=2); }", 6)


c.check("""
int printf();
int first() {
    printf("first, ");
    return 0;
}
int second() {
    printf("second, ");
    return 0;
}
int main() { return first() && second(); }
""", 0, expected_stdout="first, ")

c.check("""
int printf();
int first() {
    printf("first, ");
    return 2;
}
int second() {
    printf("second, ");
    return 0;
}
int main() { return first() && second(); }
""", 0, expected_stdout="first, second, ")

c.check("""
int printf();
int first() {
    printf("first, ");
    return 2;
}
int second() {
    printf("second, ");
    return 2;
}
int main() { return first() && second(); }
""", 1, expected_stdout="first, second, ")

c.check(r'int main() { return "\\"[0]; }', ord('\\'))
c.check(r'int main() { return "\""[0]; }', ord('\"'))
c.check(r'int main() { return "\'"[0]; }', ord('\''))
c.check(r'int main() { return "\n"[0]; }', ord('\n'))
## According to https://docs.oracle.com/cd/E19120-01/open.solaris/817-5477/eoqka/index.html 
## \a is not supported in the assembly
# c.check(r'int main() { return "\a"[0]; }', ord('\a')) 
c.check(r'int main() { return "\b"[0]; }', ord('\b'))
c.check(r'int main() { return "\t"[0]; }', ord('\t'))
c.check(r'int main() { return "\f"[0]; }', ord('\f'))
c.check(r'int main() { return "\v"[0]; }', ord('\v'))

c.check(r'int main() { return sizeof("abc\\"); }', 5)
c.check(r'int main() { return sizeof("\\abc\\"); }', 6)

c.check(r"int main() { int p = '\\'; return p; }", ord('\\'))
c.check(r"int main() { int p = '\"'; return p; }", ord('\"'))
c.check(r"int main() { int p = '\''; return p; }", ord('\''))
c.check(r"int main() { int p = '\n'; return p; }", ord('\n'))

c.check("int main() { int q; int *p = &q; return p == 0;}", 0)

c.check("int main() { int *p; p = 0; return 0;}", 0)
c.check("int main() { int *p = 0; return 0;}", 0)

c.check("int main() { int *p = 0; return !p;}", 1)
c.check("int main() { int q; int *p = &q; return !p;}", 0)

c.check("""
int printf();
int main() {
    for (int i = 1; i <= 3; i++) { 
        printf("a%d", -i); 
    }
    return 0;
}
""", 0, expected_stdout="a-1a-2a-3")

c.check("int main() { int a=1; a*=3; return a; }", 3)


c.check("int main() { return sizeof(int); }", 4)
c.check("int main() { return sizeof(int *); }", 8)
c.check("int main() { return sizeof(char); }", 1)
c.check("int main() { return sizeof(char *); }", 8)
c.check("int main() { return sizeof(char **); }", 8)

c.check(
    "int printf(); int main() { int a; int b; a=1; b=a++; printf(\"b=%d\", b); return a; }", 2, expected_stdout="b=1")
c.check(
    "int printf(); int main() { int a; int b; a=2; b=a--; printf(\"b=%d\", b); return a; }", 1, expected_stdout="b=2")

c.check("int main() { int a; a=1; a*=3; return a; }", 3)

c.check("""
int printf();
int main() {
    int i;
    for (i = 1; i <= 3; i += 1) { 
        printf("a%d", -i); 
    }
    return 0;
}
""", 0, expected_stdout="a-1a-2a-3")

c.check("""
int printf();
int main() {
    int i;
    for (i = 256; i > 1; i /= 2) { 
        printf("%d,", i); 
    }
    return 0;
}
""", 0, expected_stdout="256,128,64,32,16,8,4,2,")


c.check("""
int puts();
// line comment
int main() {
    int i; 
    /*********
     * block *
     *********/
    for (i = 1; i <= 3; i = i + 1) { 
        puts("a");//*
        // */ b 
    }
    return 0;
}
""", 0, expected_stdout="a\na\na\n")

c.check("""
int printf();
int main() {
    int i; 
    for (i = 1; i <= 3; i = i + 1) { 
        printf("a"); 
    }
    return 0;
}
""", 0, expected_stdout="aaa")

c.check("""
int printf();
int main() {
    int i;
    for (i = 1; i <= 3; i = i + 1) { 
        printf("a%d", -i); 
    }
    return 0;
}
""", 0, expected_stdout="a-1a-2a-3")

#################################

c.check("int main() { return 0; }", 0)

c.check("int main() { return 42; }", 42)

c.check("int main() { return 0+10+3; }", 0+10+3)

c.check("int main() { return 111+10-42; }", 111+10-42)

c.check("int main() { return    111   + 10 -     42; }", 111+10-42)

c.check("int main() { return    0 +    10+    3; }",  0 + 10 + 3)

c.check("int main() { return 10*2; }", 10*2)

c.check("int main() { return 10+1*2; }", 10+1*2)
c.check("int main() { return 10+3*2+10-5; }", 10+3*2+10-5)

c.check("int main() { return (10+3)*2+10-5; }", (10+3)*2+10-5)
c.check("int main() { return (10+1)*2; }", (10+1)*2)


c.check("int main() { return (10+1)/2; }", (10+1)//2)
c.check("int main() { return (15+1)/2+3; }", (15+1)//2+3)
c.check("int main() { return 10+1 /2/5; }", 10+1//2//5)

# unary
c.check("int main() { return -10+1 /2/5+30; }", -10+1//2//5+30)
c.check("int main() { return +10+1 /2/5; }", +10+1//2//5)
c.check("int main() { return -2*-3; }", -2*-3)

# equality
c.check("int main() { return 1==0; }", 0)
c.check("int main() { return 1==1; }", 1)
c.check("int main() { return 1==1+5; }", 0)
c.check("int main() { return 1+(1+1==1+1); }", 2)

c.check("int main() { return 1!=0; }", 1)
c.check("int main() { return 1!=1; }", 0)
c.check("int main() { return 1!=1+5; }", 1)

# relational
c.check("int main() { return 1>0; }", 1)
c.check("int main() { return 1>1; }", 0)
c.check("int main() { return 1<0; }", 0)
c.check("int main() { return 1<1; }", 0)
c.check("int main() { return 1>=0; }", 1)
c.check("int main() { return 1>=1; }", 1)
c.check("int main() { return 1<=0; }", 0)
c.check("int main() { return 1<=1; }", 1)


# semicolon
c.check("int main() { 1+1;return 5-2; }", 3)

# variables
c.check("int main() { int a; a=3;return a; }", 3)
c.check("int main() { int a; int b; a=3;b=4;return a+b; }", 7)

c.check("int main() { int ab; int bd; ab=3;bd=4;return ab+bd; }", 7)
c.check(
    "int main() { int abz; int bdz; abz=3;bdz =4;return abz+bdz; }", 7)

c.check("int main() { return 1;return 2; }", 1)
c.check("int main() { return 1;return 2+3; }", 1)
c.check("int main() { int a; a=0;if(1)a=1;return a; }", 1)
c.check("int main() { int a; a=0;if(0)a=1;return a; }", 0)

c.check("int main() { int a; a=1;if(a)a=5;return a; }", 5)
c.check("int main() { int a; a=0;if(a)a=5;return a; }", 0)

c.check("int main() { int a; a=1;if(a)return 5;return 10; }", 5)
c.check("int main() { int a; a=0;if(a)return 5;return 10; }", 10)

c.check(
    "int main() { int a; a=0;if(a)return 5;a=1;if(a)return 3;return 10; }", 3)
c.check("int main() { int a; a=0;while(a)return 1; return 3; }", 3)
c.check("int main() { int a; a=0;while(a<5)a=a+1; return a; }", 5)

c.check("int main() { int a; a=0;if(a)return 5;else a=10;return a; }", 10)
c.check("int main() { int a; a=1;if(a)a=0;else return 10;return a; }", 0)

c.check(
    "int main() { int a; int b; for(a=0;a<10;a=a+1)b=a;return b; }", 9)
c.check("int main() { for(;;)return 0; }", 0)

# block
c.check("int main() { { { { return 3; } } } }", 3)
c.check(
    "int main() { int a; int b; int c; a = 3; if (a) { b = 1; c = 2; } else { b = 5; c = 7; } return b + c; }", 3)
c.check(
    "int main() { int a; int b; int c; a = 0; if (a) { b = 1; c = 2; } else { b = 5; c = 7; } return b + c; }", 12)
c.check(
    "int main() { int a; int b; int c; a = 0; b = 0; c = 3; if (a) { } return c; }", 3)
c.check(
    "int main() { int a; int b; int c; a = 0; b = 0; c = 3; if (a) { if (b) { c = 2; } } return c; }", 3)
c.check(
    "int main() { int a; int b; int c; a = 0; b = 0; c = 3; if (a) { if (b) { c = 2; } } else { c = 7; } return c; }", 7)
c.check(
    "int main() { int a; int b; int c; a = 0; b = 0; c = 3; if (a) {if (b) { c = 2; } else { c = 7; }} return c; }", 3)
c.check(
    "int main() { int a; int b; int c; a = 0; b = 0; c = 3; if (a) if (b) { c = 2; } else { c = 7; } return c; }", 3)
c.check(
    "int main() { int a; int b; int c; a = 0; b = 0; c = 3; if (a) {if (b) { c = 2; }} else { c = 7; } return c; }", 7)

# link with what's built in gcc
c.check_and_link_with(
    "int identity(); int main() { return identity(3); }",
    linked_lib="int identity(int a) { return a; }",
    expected=3)

c.check_and_link_with(
    "int three(); int main() { return three(); }",
    linked_lib="int three() { return 3; }",
    expected=3)

c.check_and_link_with(
    "int add(); int main() { return add(2, 3); }",
    linked_lib="int add(int a, int b) { return a + b; }",
    expected=5)

c.check_and_link_with(
    "int add6(); int main() { return add6(1, 2, 3, 4, 5, 6); }",
    linked_lib="int add6(int a, int b, int c, int d, int e, int f) { return a + b + c + d + e + f; }",
    expected=21)

c.check("int three() { return 3; } int main() { return three(); }", 3)
c.check(
    "int one() { return 1; } int three() { return one() + 2; } int main() { return three() + three(); }", 6)
c.check(
    "int identity(int a) { return a; } int main() { return identity(3); }", 3)
c.check(
    "int add2(int a, int b) { return a + b; } int main() { return add2(1, 2); }", 3)
c.check(
    "int add6(int a, int b, int c, int d, int e, int f) { return a + b + c + d + e + f; } int main() { return add6(1, 2, 3, 4, 5, 6); }", 21)
c.check(
    "int fib(int n) { if (n <= 1) { return n; } return fib(n-1) + fib(n-2); } int main() { return fib(8); }", 21)
c.check("int main() { int x; int *y; x = 3; y = &x; return *y; }", 3)
c.check_and_link_with("int write4(); int main() { int x; x = 3; write4(&x); return x; }",
                           linked_lib="int write4(int *p) { return *p = 4; } ", expected=4)

c.check("int main() { int x; int *y; y = &x; *y = 3; return x; }", 3)


c.check_and_link_with("int alloc4(); int main() { int *p; alloc4(&p, 1, 2, 4, 8); return *(p + 0) + *(p + 1) + *(p + 2) + *(p + 3); }",
                           linked_lib="""
#include <stdlib.h>
int alloc4(int **p, int a, int b, int c, int d) { 
    *p = calloc(4, sizeof(int));
    (*p)[0] = a;
    (*p)[1] = b;
    (*p)[2] = c;
    (*p)[3] = d;
    return 0; 
} 
""", expected=15)

c.check("int main() { int x; return sizeof x; }", 4)
c.check("int main() { int *p; return sizeof p; }", 8)
c.check("int main() { int x; return sizeof(x+3); }", 4)
c.check("int main() { int *p; return sizeof(p+3); }", 8)

c.check("int main() { int arr[10]; return 8; }", 8)
c.check("int main() { int arr[10]; return sizeof(arr); }", 40)
c.check("int main() { int arr[5][2]; return sizeof(arr); }", 40)
c.check("int main() { int *arr[5][2]; return sizeof(arr); }", 80)

c.check("int main() { int arr[5][2]; return sizeof((arr)); }", 40)
c.check("int main() { int arr[5][2]; return sizeof(arr + 0); }", 8)
c.check("int main() { int arr[5][2]; return sizeof(*&arr); }", 40)

c.check("int main() { int arr[10]; return sizeof(*arr); }", 4)
c.check("int main() { int arr[5][2]; return sizeof(*arr); }", 8)
c.check("int main() { int arr[2][5]; return sizeof(*arr); }", 20)

c.check(
    "int main() { int a[2]; *a = 1; *(a + 1) = 2; int *p; p = a; return *p + *(p + 1); }", 3)
c.check(
    "int main() { int a[2]; *(a + 1) = 2; *a = 1; int *p; p = a; return *p + *(p + 1); }", 3)

c.check_and_link_with("int foo(); int main() { int a[2][4]; **a = 3; return foo(&a); }",
                           linked_lib="int foo(int (*p)[2][4]) { return (*p)[0][0] == 3; }",
                           expected=1)

c.check_and_link_with("int foo(); int main() { int a[2][4]; **(a+0) = 3; return foo(&a); }",
                           linked_lib="int foo(int (*p)[2][4]) { return (*p)[0][0] == 3; }",
                           expected=1)

c.check_and_link_with("int foo(); int main() { int a[2][4]; **(a+1) = 3; return foo(&a); }",
                           linked_lib="int foo(int (*p)[2][4]) { return (*p)[1][0] == 3; }",
                           expected=1)

c.check_and_link_with("int foo(); int main() { int a[2][4]; *(*(a+1)) = 3; return foo(&a); }",
                           linked_lib="int foo(int (*p)[2][4]) { return (*p)[1][0] == 3; }",
                           expected=1)

c.check_and_link_with("int foo(); int main() { int a[2][4]; *(*(a+1)+2) = 3; return foo(&a); }",
                           linked_lib="int foo(int (*p)[2][4]) { return (*p)[1][2] == 3; }",
                           expected=1)

c.check_and_link_with("int foo(); int main() { int a[3][4]; *(*(a+2)+1) = 4; *(*(a+1)+2) = 3; return foo(&a); }",
                           linked_lib="int foo(int (*p)[3][4]) { return (*p)[2][1] == 4 && (*p)[1][2] == 3; }",
                           expected=1)

c.check_and_link_with("int foo(); int main() { int a[1][2]; *(*(a+0)+0) = 4; *(*(a+0)+1) = 3; return foo(&a); }",
                           linked_lib="int foo(int (*p)[1][2]) { return (*p)[0][0] == 4 && (*p)[0][1] == 3; }",
                           expected=1)

c.check_and_link_with("int foo(); int main() { int a[2][2]; *(*(a+0)+0) = 4; *(*(a+0)+1) = 3; *(*(a+1)+0) = 2; *(*(a+1)+1) = 1; return foo(&a); }",
                           linked_lib="int foo(int (*p)[1][2]) { return (*p)[0][0] == 4 && (*p)[0][1] == 3 && (*p)[1][0] == 2 && (*p)[1][1] == 1; }",
                           expected=1)

c.check_and_link_with("int foo(); int main() { int i; int j; foo(5); for(i=0;i<2;i=i+1) { foo(i); } return 1; }",
                           linked_lib='''
#include <stdio.h>
int foo(int i) { printf("i=%d\\n", i); return 0; }''',
                           expected=1, expected_stdout="i=5\ni=0\ni=1\n")

c.check_and_link_with("int foo(); int main() { int p[1]; int j; *p=3; for(j=0;j<2;j=j+1) { foo(p, j); } return *p; }",
                           linked_lib='''
#include <stdio.h>
int foo(int *p, int j) { *p = j; return 0; }''',
                           expected=1)

c.check_and_link_with("int foo(); int main() { int i; int j; foo(5); for(j=0;j<2;j=j+1) { foo(j); } return 1; }",
                           linked_lib='''
#include <stdio.h>
int foo(int j) { printf("j=%d\\n", j); return 0; }''',
                           expected=1, expected_stdout="j=5\nj=0\nj=1\n")

c.check_and_link_with("int foo(); int main() { int i; int j; for(i=0;i<2;i=i+1) {for(i=0;i<4;i=i+1) { foo(i, i); } } return 1; }",
                           linked_lib='''
#include <stdio.h>
int foo(int i, int j) { printf("i=%d, j=%d\\n", i, j); return 0; }''',
                           expected=1, expected_stdout="i=0, j=0\ni=1, j=1\ni=2, j=2\ni=3, j=3\n")

c.check_and_link_with("int foo(); int main() { int i; int j; for(i=0;i<2;i=i+1) {for(j=0;j<4;j=j+1) { foo(i, j); } } return 1; }",
                           linked_lib='''
#include <stdio.h>
int foo(int i, int j) { printf("i=%d, j=%d\\n", i, j); return 0; }''',
                           expected=1, expected_stdout="""i=0, j=0
i=0, j=1
i=0, j=2
i=0, j=3
i=1, j=0
i=1, j=1
i=1, j=2
i=1, j=3
""")


c.check_and_link_with("int foo(); int main() { int a[2][4]; int i; int j; for(i=0;i<2;1) {for(j=0;j<4;1) {*(*(a + i) + j) = i * 10 + j; j=j+1;}i=i+1;} return foo(&a); }",
                           linked_lib='''
#include <stdio.h>
int foo(int (*p)[2][4]) { int i; int j; for(i=0;i<2;i++) for(j=0;j<4;j++) { printf("i=%d, j=%d, (*p)[i][j]=%d\\n", i, j, (*p)[i][j]); if ((*p)[i][j] != i * 10 + j) return i * 10 + j * 3;} return 42; }''',
                           expected=42, expected_stdout="""i=0, j=0, (*p)[i][j]=0
i=0, j=1, (*p)[i][j]=1
i=0, j=2, (*p)[i][j]=2
i=0, j=3, (*p)[i][j]=3
i=1, j=0, (*p)[i][j]=10
i=1, j=1, (*p)[i][j]=11
i=1, j=2, (*p)[i][j]=12
i=1, j=3, (*p)[i][j]=13
""")


c.check_and_link_with("int foo(); int main() { int a[2][4]; int i; int j; for(i=0;i<2;i=i+1) {for(j=0;j<4;j=j+1) {*(*(a + i) + j) = i * 10 + j;}} return foo(&a); }",
                           linked_lib='''
#include <stdio.h>
int foo(int (*p)[2][4]) { int i; int j; for(i=0;i<2;i++) for(j=0;j<4;j++) { printf("i=%d, j=%d, (*p)[i][j]=%d\\n", i, j, (*p)[i][j]); if ((*p)[i][j] != i * 10 + j) return i * 10 + j * 3;} return 42; }''',
                           expected=42, expected_stdout="""i=0, j=0, (*p)[i][j]=0
i=0, j=1, (*p)[i][j]=1
i=0, j=2, (*p)[i][j]=2
i=0, j=3, (*p)[i][j]=3
i=1, j=0, (*p)[i][j]=10
i=1, j=1, (*p)[i][j]=11
i=1, j=2, (*p)[i][j]=12
i=1, j=3, (*p)[i][j]=13
""")


c.check_and_link_with("int foo(); int main() { int a[2][4]; int i; int j; for(i=0;i<2;i=i+1) for(j=0;j<4;j=j+1) *(*(a + i) + j) = i * 10 + j; return foo(&a); }",
                           linked_lib='''
#include <stdio.h>
int foo(int (*p)[2][4]) { int i; int j; for(i=0;i<2;i++) for(j=0;j<4;j++) { printf("i=%d, j=%d, (*p)[i][j]=%d\\n", i, j, (*p)[i][j]); if ((*p)[i][j] != i * 10 + j) return i * 10 + j * 3;} return 42; }''',
                           expected=42, expected_stdout="""i=0, j=0, (*p)[i][j]=0
i=0, j=1, (*p)[i][j]=1
i=0, j=2, (*p)[i][j]=2
i=0, j=3, (*p)[i][j]=3
i=1, j=0, (*p)[i][j]=10
i=1, j=1, (*p)[i][j]=11
i=1, j=2, (*p)[i][j]=12
i=1, j=3, (*p)[i][j]=13
""")

c.check_and_link_with("int foo(); int main() { int a[2][4]; int i; int j; for(i=0;i<2;i=i+1) {for(j=0;j<4;j=j+1) {a[i][j] = i * 10 + j;}} return foo(&a); }",
                           linked_lib='''
#include <stdio.h>
int foo(int (*p)[2][4]) { int i; int j; for(i=0;i<2;i++) for(j=0;j<4;j++) { printf("i=%d, j=%d, (*p)[i][j]=%d\\n", i, j, (*p)[i][j]); if ((*p)[i][j] != i * 10 + j) return i * 10 + j * 3;} return 42; }''',
                           expected=42, expected_stdout="""i=0, j=0, (*p)[i][j]=0
i=0, j=1, (*p)[i][j]=1
i=0, j=2, (*p)[i][j]=2
i=0, j=3, (*p)[i][j]=3
i=1, j=0, (*p)[i][j]=10
i=1, j=1, (*p)[i][j]=11
i=1, j=2, (*p)[i][j]=12
i=1, j=3, (*p)[i][j]=13
""")

c.check("int main() { int a; int b; a = b = 3; return a + b; }", 6)

c.check("int *foo; int bar[10]; int main() { return 0; }", 0)

c.check(
    "int *foo; int bar[10]; int main() { foo = bar; bar[3] = 7; return foo[3]; }", 7)

c.check(
    "int main() { char x[3]; x[0] = -1; x[1] = 2; int y; y = 4; return x[0] + y; }", 3)

c.check("int main() { char *x; x = \"@A\"; return x[1] - x[0]; }", 1)
c.check("int main() { char *x; x = \"az\"; return x[1] - x[0]; }", 25)
c.check("int main() { return \"az\"[1] - \"ab\"[0]; }", 25)