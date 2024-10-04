clear all;close all;clc;
I=imread('rice.png');
[m,n]=size(I);
for i=1:256
    p(i)=0;
end
    for i=1:m
    for j=1:n
        x=I(i,j);
        p(x+1)=p(x+1)+1;
    end
    end
N=m*n;
pi=p/N;
sigB=zeros(1,256);
for k=1:256
    p1=0;
for i=1:k
    p1=p1+pi(i);
end
p2=0;
for j=k+1:256
    p2=p2+pi(j);
end
t1=0;
for i=1:k
    t1=t1+i*pi(i);
end
m1=t1/p1;
t2=0;
for i=k+1:256
    t2=t2+i*pi(i);
end
m2=t2/p2;
Mg=p1*m1+p2*m2;
sigB(k)=p1*p2*(m1-m2)^2;
end
maximum = max(sigB);
[x,y]=find(sigB==maximum);
th=y-1;
g=(I>th);
figure,imshow(g)