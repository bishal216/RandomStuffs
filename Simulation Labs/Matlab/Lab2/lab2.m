h=0.0002;
v10=0.0;
v20=0.0;
n = 500
a11=-50;
a21=-10000;
a22=-21.5;

ein = 2

v1=zeros(1,n);
v2=zeros(1,n);
t=zeros(1,n);

for i=1:n
    m11=func1(a11,v10,ein);
    m12=func1(a11,v10+m11*h/2,ein);
    m13=func1(a11,v10+m12*h/2,ein);
    m14=func1(a11,v10+m13*h,ein);
    v11=v10+((m11+2*m12+2*m13+m14)/6)*h;
    v1(i)=v11;
        
    m21=func2(v10,v20,a21,a22,ein);
    m22=func2(v10+h/2,v20+m21*h/2,a21,a22,ein);
    m23=func2(v10+h/2,v20+m22*h/2,a21,a22,ein);
    m24=func2(v10+h,v20+m23*h,a21,a22,ein);
    v21=v20+((m21+2*m22+2*m23+m24)/6)*h;
    v2(i)=v21;
        
    t(i)=h*i;
    v10=v11;
    v20=v21;
end
subplot(2,1,1)
plot(t,v1)

subplot(2,1,2)
plot(t,v2)
