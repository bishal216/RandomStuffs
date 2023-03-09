clf
clearvars
a=7;
b=21;
P=64;

r(1)=17;
N = 64
for i=1:N-1
    r(i+1) = mod(r(i)*a+b,P)
end
x = 1:N
hold on
plot(x,r)
scatter(x,r)
hold off

n = 8
Ei = N/n
Oi = zeros(1,n)
h = P/n
for i=1:N
    j = floor(r(i)/h)+1
    Oi(j)= Oi(j)+1
end
x2 = 0
for i = 1:n
    x2 = x2+ ((Oi(i) - Ei)^2)/Ei
end