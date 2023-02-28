from test import bcolors, check, check_and_link_with

print(f"{bcolors.WARNING}Checking the inputs that SHOULD work, but is currently REJECTED:{bcolors.ENDC}")

print(f"{bcolors.OKCYAN}escape sequence{bcolors.ENDC}")
check(r"int main() { return '\a';}", 7)

print(f"{bcolors.OKCYAN}bitwise operations{bcolors.ENDC}")
check("int main() { return 5 | 6; }", 7)
check("int main() { return 5 & 6; }", 4)
check('int main(){return 175^1;}' , 174)
check('int main(){3; {5; 7; 11; } return 175^1;}' , 174)

print(f"{bcolors.OKCYAN}enum & union{bcolors.ENDC}")
check('enum Foo { ZERO } foo() { return ZERO; } int main() { int a = foo(); return a; }' , 0)
check('union A { char a[7]; int b; }; int main(void) { return sizeof(union A); }' , 8)
check('union A { char a[4]; int b; }; int main(void) { union A x; x.a[0] = 0x4b; x.a[1] = 0x6f; x.a[2] = 0x72; x.a[3] = 0x79; return x.b - 0x79726f4b; }' , 0)
check('enum A{B, C}; int main(void){ enum A b; return 174; }' , 174)
check('enum A{B, C,}; int main(void){ enum A b; return 174; }' , 174)
check('enum A{B, C,}; int main(void){ enum A b; b = 5; return 174; }' , 174)
check('enum A{B, C,}; int main(void){ enum A b; b = B; return 174+b; }' , 174)
check('enum A{B, C,D}; int main(void){ enum A b; b = D; return 172+b; }' , 174)

print(f"{bcolors.OKCYAN}label & goto{bcolors.ENDC}")
check('int main() { int a; goto a; if (0) { a: a = 3; } else { a = 7; } return a; }' , 3)
check('int main() { int a; goto a; if (1) { a = 3; } else { a: a = 7; } return a; }' , 7)
check('int main() {goto a; return 3; a: return 0;} ' , 0)
check('int main(){ int i = 3; goto a; for (i = 0; i < 10; i++) { a: return i; } }' , 3)
check('int main(void){ foo: return 174;}' , 174)
check('int main(void){ foo: bar: return 174;}' , 174)
check('int main(void){ foo: {baz: hoge: 1;} bar: return 174;}' , 174)

print(f"{bcolors.OKCYAN}ternary operator{bcolors.ENDC}")
check('int foo(void) { return 3; } int bar(void) { return 5;} int main(void) { int (*foo1)(void) = foo; int (*bar1)(void) = bar; return (1? foo1 : bar1)(); }' , 3)
check('int foo(void) { return 3; } int main(void) { return (1? foo : 0)(); }' , 3)
check('int foo(void) { return 3; } int bar(void) { return 5;} int main(void) { return (1? foo : bar)(); }' , 3)
check('int foo(void) { return 3; } int bar(void) { return 5;} int main(void) { return (0? foo : bar)(); }' , 5)
check('int main(){int a = 1; int *b = a?&a : 0; return 123;}' , 123)
check('int main(){int a = 1; int *b = a? 0 :&a; return 123;}' , 123)
check('int main(){int a = 0; int *b = a?&a : 0; return 123;}' , 123)
check('int main(){int a = 0; int *b = a? 0 :&a; return 123;}' , 123)
check('struct A{int a; int b; int *q; int *t; int *p;}; struct A f(void) {struct A u; u.a = 100;return u;} int main(void){struct A u = f(); struct A v; v.a = 1; return (1? u : v).a + 74;}' , 174)
check('struct A{int a; int b; int *q; int *t; int *p;}; struct A f(void) {struct A u; u.a = 100;return u;} int main(void){struct A u = f(); struct A v; v.a = 1; return (0? u : v).a + 74;}' , 75)
check('int main(){int *p; int a; p = &a; return p?174:1;}' , 174)
check('int main(){int *p; p = 0; return p?174:1;}' , 1)
check('int a(int b){ return b; }int main(){int i; i=1; a(i == 1? 1 : 2); return 0;}' , 0)
check('int a(int b){ return b; }int main(){int i; for (i = 1; i < 11; i++) { a(i == 1? 1 : 2); } return 0;}' , 0)
check('int a(int b){ return b; }int main(){int i; i=1; return a(i == 1? 174 : 2);}' , 174)
check('int printf();int puts();int count;int main(){int i; int hist[20]; for (i = 1; i < 11; i++) { printf(i == 1? "a" : "b"); puts("");} return 0;}' , 0)
check('int printf();int puts();int count;int main(){int i; int hist[20]; for (i = 1; i < 11; i++) { printf("%s", (i == 1? "a" : "b")); puts("");} return 0;}' , 0)
check('int printf();int puts();int count;int main(){int i; int hist[20]; for (i = 1; i < 11; i++) { printf("%d %s: %d", i, (i == 1? " " : "s "), i); puts("");} return 0;}' , 0)
check('int main(){return 2 + (1? 100 + 72 : 17);}' , 174)
check('int main(){return (0? 234 : 2) + (1? 100 + 72 : 17);}' , 174)
check('int fib(int n){ return n < 2? n : fib(n - 1) + fib(n - 2); } int main(){3; return fib(10);}' , 55)
check('int tarai(int x,int y,int z){ return x <= y? y : tarai(tarai(x-1, y, z), tarai(y-1, z, x), tarai(z-1, x, y)); } int main(){return tarai(12,6,0);}' , 12)

print(f"{bcolors.OKCYAN}comma operator{bcolors.ENDC}")
check('struct A{int a; int b; int *q; int *t; int *p;}; struct A f(void) {struct A u; u.a = 100;return u;} int main(void){struct A u = f(); return (u, 174);}' , 174)
check('struct A{int a; int b; int *q; int *t; int *p;}; struct A f(void) {struct A u; u.a = 100;return u;} int main(void){struct A u = f(); return (1,u).a + 74;}' , 174)
check('struct A{int a; int b; int *q; int *t; int *p;}; struct A f(void) {struct A u; u.a = 100;return u;} int main(void){struct A u = f(); return (1,2,u).a + 74;}' , 174)
check('int main(){int a; int b; for(a=0,b=0;a <= 10;) {b += a; a += 1;}return b;}' , 55)
check('int main(){int a; int b; for(a=0,b=0;a <= 10;++a) {b += a;}return b;}' , 55)
check('int main(){int a; int b; for(a=0,b=0;a <= 10;a++) {b += a;}return b;}' , 55)
check('int main(){int a; int b; return (a = b = 9, a = 41*3, 55 - (b = 4) + a);}' , 174)
check('int main(){int a; int b; int c; int d; int _q432; a = b = c = 9; d = 5; a = 41*3; return (c, _q432 = 8, d = 11*5) - (b = 4) + a;}'  , 174)
check('int main(){return 043,41*3+07*010-0Xa/(010%(!!1+2));}' , 174)
check('int main(){return 43,6*(3+7)-5*1;}' , 55)
check('int main(){return 43,6*(3+(4|3))-(5|1)*1;}' , 55)
check('int main(){return 043,41*3+07*010-0Xa/(010%(1+2));}' , 174)
check('int main(){return 7*5,(12,41*3)+7*16/(9,2)-10/(8%3);}' , 174)

print(f"{bcolors.OKCYAN}prefix increment / decrement{bcolors.ENDC}")
check('int main(){int a; int b; a=3; b=0; b+= ++a; return a*b*11-2;}' , 174)
check('int a; int main(){int *p; p = &a; int i; for(i=0;i<174;i++){++*p;} return a;}' , 174)
check('int a; int main(){int *p; p = &a; int i; for(i=0;i<174;((i))++){++*p;} return a;}' , 174)
check('int main(void){int a[5]; a[3] = 174; int *p = a + 2; ++p; return *p;}' , 174)
check('int main(void){int a[5]; a[3] = 174; int *p = a + 2; return *++p;}' , 174)
check('int main(void){char a[5]; a[1] = 74; char *p = a + 2; return *--p;}' , 74)

print(f"{bcolors.OKCYAN}__func__{bcolors.ENDC}")
check('int main() {return __func__[1] - 97;} ' , 0)

print(f"{bcolors.OKCYAN}unhandlable size{bcolors.ENDC}")
check('struct A3 {char a[3];}; struct A3 deref3(struct A3 *p){ return *p;} int main(){return 3;}' , 3)
check('struct A{int a; int b; int *q; int *t; int *p;}; struct A f(void) {struct A u; u.a = 100;return u;} int main(void){struct A u = f(); struct A v; return (v = u).a + 74;}' , 174)
check('struct A{int a; int b; int *q; int *t; int *p;}; struct A f(void) {struct A u; u.a = 100;return u;} int main(void){struct A u = f(); return u.a + 74;}' , 174)
check('struct A{int a; int b; int *q; int *r; int *s; int *t; int *p;}; struct A f(void) {struct A u; u.a = 100; u.b = 74; u.p = 0; return u;} int main(void){struct A u = f(); struct A *p = &u; if (u.p) {return 3;} else {return p->a + p->b;}}' , 174)
check('struct A{int a; int b; int *p;}; struct A f(void) {struct A u; u.a = 100; u.b = 74; u.p = 0; return u;} int main(void){struct A u = f(); struct A *p = &u; if (u.p) {return 3;} else {return p->a + p->b;}}' , 174)
check('struct A{int a; int b; int *p;}; struct A f(void) {struct A u; u.a = 100; u.b = 74; u.p = 0; return u;} int g (struct A *p) {return p->a + p->b;} int main(void){struct A u = f(); struct A *p = &u; if (u.p) {return 3;} else {return g(p);}}' , 174)
check('struct A{int a; int b; int *p;}; struct A f(int j) {struct A u; u.a = 100; u.b = 72 + j; u.p = 0; return u;} int g (struct A *p) {return p->a + p->b;} int main(void){struct A u = f(2); struct A *p = &u; if (u.p) {return 3;} else {return g(p);}}' , 174)
check('struct A{int a; int b; int *p;}; struct A f(void) {struct A u; u.a = 100; u.b = 74; u.p = 0; return u;} int main(void){struct A u = f(); if (u.p) {return 3;} else {return u.a + u.b;}}' , 174)
check('struct A{int a; int *b; int c;}; struct B{char d; struct A e;}; int main(){struct A a; a.a = 174; struct B b; b.e = a; return b.e.a;}' , 174)
check('struct A{int a; int *b; int c;}; struct B{char d; struct A e;}; int main(){struct A a; a.a = 174; struct B b; b.e = a; return (b.e).a;}' , 174)
check('struct A{int a; int *b; int c;}; struct B{char d; struct A e;}; int main(){struct A a; a.a = 174; struct B b; b.e.a = 174; a = b.e; return a.a;}' , 174)
check('struct A{char a; int b; char c;}; int main(){struct A a; a.c = 74; struct A b = a; return b.c;}' , 74)
check('int changeBoard(int board[30][30], int i, int j, int d, int N){int k;for (k = 0; k < N; k++) {*(*(board + i) + k) += d;*(*(board + k) + j) += d;}if (i > j) {for (k = 0; k < N - (i - j); k++) {*(*(board + k + (i - j)) + k) += d;}} else {for (k = 0; k < N - (j - i); k++) {*(*(board + k) + k + (j - i)) += d;}}if (i + j < N) {for (k = 0; k <= i + j; k++) {*(*(board + i + j - k) + k) += d;}} else {for (k = i + j - N + 1; k < N; k++) {*(*(board + i + j - k) + k) += d;}}return 0;}int setQueen(int board[30][30], int num_placed, int *ptr_sol_num, int N){int j;if (num_placed == N) {(*ptr_sol_num)+=1;return 0;}for (j = 0; j < N; j++) {if (*(*(board+num_placed)+j) == 0) {changeBoard(board, num_placed, j, +1, N);setQueen(board, num_placed + 1, ptr_sol_num, N);changeBoard(board, num_placed, j, -1, N);}}return 0;}int board_[30][30];int main(){int sol_num;sol_num = 0;setQueen(board_, 0, &sol_num, 8);return sol_num;}' , 92)
check('int changeBoard(int board[30][30], int i, int j, int d, int N){int k;for (k = 0; k < N; k++) {board[i][k] += d;board[k][j] += d;}if (i > j) {for (k = 0; k < N - (i - j); k++) {board [k + (i - j)][k] += d;}} else {for (k = 0; k < N - (j - i); k++) {board[k][k + (j - i)] += d;}}if (i + j < N) {for (k = 0; k <= i + j; k++) {board[i + j - k][k] += d;}} else {for (k = i + j - N + 1; k < N; k++) {board[i + j - k][k] += d;}}return 0;}int setQueen(int board[30][30], int num_placed, int *ptr_sol_num, int N){int j;if (num_placed == N) {(*ptr_sol_num)+=1;return 0;}for (j = 0; j < N; j++) {if (board[num_placed][j] == 0) {changeBoard(board, num_placed, j, +1, N);setQueen(board, num_placed + 1, ptr_sol_num, N);changeBoard(board, num_placed, j, -1, N);}}return 0;}int board_[30][30];int main(){int sol_num;sol_num = 0;setQueen(board_, 0, &sol_num, 8);return sol_num;}' , 92)
check('int a[10][10]; int foo(int p[10][10]){int q;q = p++[0][0]; return q+p[0][0];} int main(){a[0][0] = 100; a[1][0] = 74; return foo(a);}' , 174)
check('int a[10][10]; int foo(int p[10][10]){int q;q = ((p+=1)-1)[0][0]; return q+p[0][0];} int main(){a[0][0] = 100; a[1][0] = 74; return foo(a);}' , 174)

print(f"{bcolors.OKCYAN}complicated type definition (ptr to array, ptr to function){bcolors.ENDC}")
check('struct A {int k[15];}; int main(){struct A s; int (*p)[15] = &s.k; return 35;}' , 35)
check('struct A {int k[15];}; struct A f(int a, int b){struct A q; q.k[0] = a; q.k[14] = b; return q;} int main(){struct A (*g)(int a, int b) = f; struct A q = g(10, 11); return q.k[0] + q.k[14]; }' , 21)
check('struct A {int a; int b;}; struct A f(int a, int b){struct A q; q.a = a; q.b = b; return q;} int main(){ struct A (*g)(int, int) = f; struct A q = g(100, 74); return q.a + q.b;}' , 174)
check('int puts(const char *str); int atoi(const char *str); int f(int a){int (*arr[2])(const char *str);arr[0] = &puts;arr[1] = &atoi;return arr[a]("123");} int main(){f(0); return f(1);}' , 123)
check('int puts(const char *str); int atoi(const char *str); int f(int a){int (*arr[2])(const char *str);arr[0] = puts;arr[1] = atoi;return arr[a]("123");} int main(){f(0); return f(1);}' , 123)
check('int main(){void *null = 0; int (*p)(void) = null; return 123;}' , 123)
check('int main(){void *null = 0; int (*p)(int) = null; return 123;}' , 123)
check('int main(void) {int a[5]; a[3] = 174; int (*p)[5] = &a; return (*p)[3];} ' , 174)
check('int changeBoard(int (*board)[30], int i, int j, int d, int N){int k;for (k = 0; k < N; k++) {*(*(board + i) + k) += d;*(*(board + k) + j) += d;}if (i > j) {for (k = 0; k < N - (i - j); k++) {*(*(board + k + (i - j)) + k) += d;}} else {for (k = 0; k < N - (j - i); k++) {*(*(board + k) + k + (j - i)) += d;}}if (i + j < N) {for (k = 0; k <= i + j; k++) {*(*(board + i + j - k) + k) += d;}} else {for (k = i + j - N + 1; k < N; k++) {*(*(board + i + j - k) + k) += d;}}return 0;}int setQueen(int (*board)[30], int num_placed, int *ptr_sol_num, int N){int j;if (num_placed == N) {(*ptr_sol_num)+=1;return 0;}for (j = 0; j < N; j++) {if (*(*(board+num_placed)+j) == 0) {changeBoard(board, num_placed, j, +1, N);setQueen(board, num_placed + 1, ptr_sol_num, N);changeBoard(board, num_placed, j, -1, N);}}return 0;}int board_[30][30];int main(){int sol_num;sol_num = 0;setQueen(board_, 0, &sol_num, 8);return sol_num;}' , 92)
check('int changeBoard(int (*board)[30], int i, int j, int d, int N){int k;for (k = 0; k < N; k++) {board[i][k] += d;board[k][j] += d;}if (i > j) {for (k = 0; k < N - (i - j); k++) {board [k + (i - j)][k] += d;}} else {for (k = 0; k < N - (j - i); k++) {board[k][k + (j - i)] += d;}}if (i + j < N) {for (k = 0; k <= i + j; k++) {board[i + j - k][k] += d;}} else {for (k = i + j - N + 1; k < N; k++) {board[i + j - k][k] += d;}}return 0;}int setQueen(int (*board)[30], int num_placed, int *ptr_sol_num, int N){int j;if (num_placed == N) {(*ptr_sol_num)+=1;return 0;}for (j = 0; j < N; j++) {if (board[num_placed][j] == 0) {changeBoard(board, num_placed, j, +1, N);setQueen(board, num_placed + 1, ptr_sol_num, N);changeBoard(board, num_placed, j, -1, N);}}return 0;}int board_[30][30];int main(){int sol_num;sol_num = 0;setQueen(board_, 0, &sol_num, 8);return sol_num;}' , 92)
check('int main(){int a[5][6];int (*p)[6];p = a;int *q;q = p[1]; 2[q]=174; return 1[a][2];}' , 174)
check('int *foo(int *(p)){*p = 4;return p;} int main(){int (x);int (y); int (*(*(z))); *foo(&x) += 170;return x;}' , 174)
check('int main(){int a[1][2];int (*p)[2];p = a;int *q;q = *p;return 174;}' , 174)
check('int main(){int a[1][2];int (*p)[2];p = a;int *q;q = *p; *q=174; return **a;}' , 174)
check('int main(){int a[74][2];int (*p)[2];p = a;int *q;q = *(p+1); *q=174; return **(a+1);}' , 174)
check('int main(){int a[5][6];int (*p)[6];p = a;int *q;q = *(p+1); *(2+q)=174; return *(*(1+a)+2);}' , 174)
check('int (*func(int (*a)[5]))[5]{return a;} int main(){int a[6][5]; a[1][2] = 174; return func(a)[1][2];}' , 174)

print(f"{bcolors.OKCYAN}complicated type definition (sizeof on an array type){bcolors.ENDC}")
check('struct A{int a; int *b; int c;}; int main(){return sizeof(struct A [5]);}' , 120)
check('struct A{int a; int *b; int c;}; struct B{char d; struct A e;}; int main(){return sizeof(struct B [4]);}' , 128)

print(f"{bcolors.OKCYAN}function pointer{bcolors.ENDC}")
check('int foo() { return 0; } int main(){(foo)(); return 0;}' , 0)
check('int printf(); int main(){(printf)("Hello, World!"); return 0;}' , 0)
check('int printf(); int main(){(**************printf)("Hello, World!"); return 0;}' , 0)

print(f"{bcolors.OKCYAN}switch{bcolors.ENDC}")
check('int main(void){ int a; a = 174; switch(1){a = 2; 1;} return a;}' , 174)
check('int main(void){ int a; a = 174; switch(1){a = 2; break; a = 3;} return a;}' , 174)
check('int main(void){ int a; a = 1; int b; b = 0; switch(1){ b = 15; default: a = 174; break; a = 3;} return a+b ;}' , 174)
check('int main(void){ switch(1){ if(0){ default: return 174; } } return 3; }' , 174)
check('int main(void){ int a; a = 1; switch(1){ default: a = 173; switch(0){ default: return a+1; } return 5; } return 3; }' , 174)
check('int main(void){ int a; a = 1; switch(1){ case 1: a = 174; } return a; }' , 174)
check('int main(void){ int a; a = 174; switch(2){ case 1: a = 1; } return a; }' , 174)
check('int f(int a){switch(a){case 1: return 3; case 2: return 5; default: return 8;}} int main(void){ return (f(1)-3) || (f(2)-5) || (f(3)-8) || (f(100)-8);}' , 0)
check('int main(void){ char a; a = 0; switch(a){case 0: a = 174; break; case 256: a = 3; break; default: a = 5; break;}  return a;}' , 174)
check('enum A{B, C,D}; int f(enum A b){switch(b){case B: return 1; case C: return 5; case D: return 8;}} int main(void){ return (f(B) - 1) || (f(C) - 5) || (f(D) - 8);}' , 0)

print(f"{bcolors.OKCYAN}_Alignof{bcolors.ENDC}")
check('int main(){return _Alignof(int);}' , 4)
check('int main(){return _Alignof(int*);}' , 8)
check('struct A{int a; int b;}; int main(){ return _Alignof(struct A);}' , 4)
check('struct A{int a; char c; char d; int b;}; int main(){ return _Alignof(struct A);}' , 4)
check('struct A{int a; int *b; int c;}; int main(){return _Alignof(struct A [5]);}' , 8)

print(f"{bcolors.OKCYAN}static{bcolors.ENDC}")
check('static int hidden() { return 3;} int main(){return 171 + hidden();}' , 174)

print(f"{bcolors.OKCYAN}do-while{bcolors.ENDC}")
check('int foo(){return 1;} int main(){int a; a=0;do{a=3;}while(a==foo());return 174;}' , 174)
check('int main(){int a; a=0;do{a+=1;}while(a && a < 174);return a;}' , 174)
check('int main(){int a; a=-8;do{a+=1;}while(a);return a+174;}' , 174)
check('int main(){int a; int b; a =0; b=0; do{a-=1;b+=a;if(a)continue;break; a+=100;}while(a+3); return -a;}' , 3)
check('int main(){int a; int b; a =0; b=0; do{a-=1;b+=a;if(a)continue;break; a+=100;}while(a+3); return -b;}' , 6)
check('int main(){int a; int b; a =0; b=0; do{a-=1;b+=a;if(a)continue;break; a+=100;}while(a+3); return a*b*10;}' , 180)
check('int main(){int a; int b; a =0; b=0; do{a-=1;b+=a;if(a)continue;break; a+=100;}while(a+3); return a*b*10+a+b+3;}' , 174)
check('int main(){int a; int b; a =0; b=0; do{a-=1;b+=a;if(a)continue;break; a+=100;}while(a+3); return a*b;}' , 18)
check('int main(){int a; int b; a =0; b=0; do{a-=1;b+=a;if(a)continue;break; a+=100;}while(a+3); return b*a;}' , 18)
check('int main(){int a; int b; a =0; b=0; do{a-=1;b+=a;if(a)continue;break; a+=100;}while(a+3); return b*a*10;}' , 180)
check('int main(){int a; int b; a =0; b=0; do{a-=1;b+=a;if(a)continue;break;}while(a+3); return a*b;}' , 18)
check('int main(){int a; int b; a =0; b=0; do{a-=1;b+=a;if(!a)break;}while(a+3); return a*b;}' , 18)
check('int main(){int a; int b; a =0; b=0; do{a-=1;b+=a;}while(a+3); return a*b;}' , 18)
check('int main(){int a; int b; a =0; b=0; do{a-=1;b+=a;}while(a+3); return b*a;}' , 18)
check('int main(){int a; int b; a =0; b=0; do{b+=--a;}while(a+3); return b*a;}' , 18)

print(f"{bcolors.OKCYAN}continue & break{bcolors.ENDC}")
check('int main(){int a; a = 3;while (a) {a = 2;if (a - 3) {break;}a += 3;}return 174;}' , 174)
check('int main(){int a; int b; int c; a = 3; b = 5; c = 0;while(a){while(b) {c += b;b-=1;if(b == 3) break;}b = 7;a-=1;if(a == 1) break;} return a*7+b*15+c*2;}' , 174)
check('int main(){int a; a = 3;while (a) {a = 2;if (a - 3) {break;}a += 3;}return 174;}' , 174)
check('int main(){int a; int b; a=11; b=0; while(a){a-=1;b+=a;if(a)continue;break; a+=100;} return b;}' , 55)
check('int main(){int a; for (a = 3;a;) {a = 2;if (a - 3) {break;}a += 3;}return 174;}' , 174)
check('int main(){int a; for (a = 3;;) {a = 2;if (a - 3) {break;}a += 3;}return 174;}' , 174)
check('int main(){int a; int b; for(a=11, b=0;a;){a-=1;b+=a;if(a)continue;break; a+=100;} return b;}' , 55)
check('int main(){int a; int b; int c; int d; d=0; b = 5; c = 0;for(a = 3;a;d++){for(;b;++d) {c += b;b-=1;if(b == 3) break;}b = 7;a-=1;if(a == 1) break;} return a*7+b*15+c*2;}' , 174)
check('int printf();int puts();int count;int solve(int n, int col, int *hist){if (col == n) {count+=1;return 0;}int i;int j;for (i = 0, j = 0; i < n; i++) {for (j = 0; j < col && hist [j] != i && (hist [j] - i) != col - j && (hist[j] - i) != j - col; j++){}if (j < col)continue;hist[col] = i;solve(n, col + 1, hist);}return 0;}int main(){int i; int hist[20]; for (i = 1; i < 11; i++) { count=0; solve(i, 0, hist); printf("%d queen%s: %d", i, (i == 1? " " : "s "), count); puts("");} return 0;}' , 0)
check('int printf();int puts();int count;int solve(int n, int col, int *hist){if (col == n) {count+=1;return 0;}int i;int j;for (i = 0, j = 0; i < n; i++) {for (j = 0; j < col && hist [j] != i && (hist [j] - i) != col - j && (hist[j] - i) != j - col; j++){}if (j < col)continue;hist[col] = i;solve(n, col + 1, hist);}return 0;}int main(){int i; int hist[20]; for (i = 2; i < 11; i++) { count=0; solve(i, 0, hist); printf("%d queens: %d", i, count); puts("");} return 0;}' , 0)
check('int count;int solve(int n, int col, int *hist){if (col == n) {count+=1;return 0;}int i;int j;for (i = 0, j = 0; i < n; i++) {for (j = 0; j < col && *(hist + j) != i && (*(hist + j) - i) != col - j && (*(hist + j) - i) != j - col; j++){}if (j < col)continue;*(hist+col) = i;solve(n, col + 1, hist);}return 0;}int main(){int hist[8];solve(8, 0, hist);return count;}' , 92)
check('int count;int solve(int n, int col, int *hist){if (col == n) {count+=1;return 0;}int i;int j;for (i = 0, j = 0; i < n; i++) {for (j = 0; j < col && *(hist + j) != i && (hist [j] - i) != col - j && (*(hist + j) - i) != j - col; j++){}if (j < col)continue;*(hist+col) = i;solve(n, col + 1, hist);}return 0;}int main(){int hist[8];solve(8, 0, hist);return count;}' , 92)
check('int count;int solve(int n, int col, int *hist){if (col == n) {count+=1;return 0;}int i;int j;for (i = 0, j = 0; i < n; i++) {for (j = 0; j < col && hist [j] != i && (hist [j] - i) != col - j && (hist[j] - i) != j - col; j++){}if (j < col)continue;hist[col] = i;solve(n, col + 1, hist);}return 0;}int main(){int hist[8];solve(8, 0, hist);return count;}' , 92)
check('int main(){int a; int b; for(a=0,b=0;a<10;a++){ if(a ==5)continue;b+=a;} return b;}' , 40)

print(f"{bcolors.OKCYAN}juxtaposed string literals{bcolors.ENDC}")
check('int printf(); int puts(); int main(){printf("H""e" "l" "lo," " W" "or" "ld!"); puts(""); return 174;}' , 174)

print(f"{bcolors.OKCYAN}bitshift{bcolors.ENDC}")
check('int main() {int a; int b; int c; a = 7; a &= ~2; a <<= 2; a |=2; a >>= 1; a -=5; a /= 2; b = 3; c = 8; b ^= (c%=3); b *= (a += 5);  return a + b + 158; }' , 174)

print(f"{bcolors.OKCYAN}tab character{bcolors.ENDC}")
check('int main(){return 7*5 	,	(0xC,(41   )*(4-(011>8)))+7*(((1+2)>=3)<<4)/(9,(4>>(10<=10))+(3<3))-10/(	  ( 	1  <<3)	%3);}'  , 174)
check('int main(){return 35,	((	41|	(8   !=     15))*  ((3==3)+2))+((5|2)*(9&10))   -   (10/(8%3));}'  , 174)
check('int main(){return 7*5 	,	(0xC,(41   )*(4-(011>8)))+7*(((1-~1)>=3)<<4)/(9,(4>>(10<=10))+(3<3))-10/(	  ( 	!0  <<3)	%3);}' , 174)

print(f"{bcolors.OKCYAN}hex literal{bcolors.ENDC}")
check('int main(){return 0x29*3+7*8-5*1;}' , 174)

print(f"{bcolors.OKCYAN}empty variable definition{bcolors.ENDC}")
check('char; char     ; char; int; int ; int; int;int;char foo(char *p){char a; return a;} int main(){char q; foo(&(q)); return 174;}' , 174)
check(' struct A; char; char     ; char; int; int ; int; struct B;  int;int;  struct C; int main(){return 174;}' , 174)
check(' struct A{int a; int b;}; char; char     ; char; int; int ; int; struct B{int c; int b;};  int;int;  struct C; int main(){return 174;}' , 174)
check('int main(){ int; return 174;}' , 174)
check('struct A{int a; int b;}; int main(){ struct A; return 174;}' , 174)

print(f"{bcolors.OKCYAN}`const` positioned in a rare position{bcolors.ENDC}")
check('struct A {int a;};int main(){const struct A const *const a; return 174;}' , 174)
check('struct A {int a;};int f(int *const b){return 0;}int main(){const struct A const *const a; return 174;}' , 174)
check('struct A {int a;};const int f(const int *const b){return 0;}int main(){const struct A const *const a; return 174;}' , 174)

print(f"{bcolors.OKCYAN}global variable with an initializer{bcolors.ENDC}")
check('int a = 3; int main() { return 0; }', 0)

print(f"{bcolors.OKCYAN}cast{bcolors.ENDC}")
check('int main() { return (int)3; }', 3)

print(f"{bcolors.OKCYAN}typedef{bcolors.ENDC}")
check('typedef int A; int main() { return sizeof(A); }', 4)
check('typedef struct A { int a; } A; int main() { A a; return 0; }', 0)

print(f"{bcolors.OKCYAN}struct declaration{bcolors.ENDC}")
check('struct A; int main(){ return 0; }', 0)

print(f"{bcolors.OKCYAN}more than 6 args / params{bcolors.ENDC}")
check("int foo(int a1, int a2, int a3, int a4, int a5, int a6, int a7) { return 0; } int main() { return 7; }", 7)
check_and_link_with("int foo(); int main() { return foo(1,2,3,4,5,6,7); }", "int foo(int a1, int a2, int a3, int a4, int a5, int a6, int a7) { return 0; }", 7)
