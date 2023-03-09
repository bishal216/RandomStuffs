clf
dt=0.01;
t=0:dt:1;
n=length(t);

K1=1;
K2=1;

C1=zeros(n);
C2=zeros(n);
C3=zeros(n);

C1(1) = 12;
C2(1) = 7;
C3(1) = 3;
for i=2:n
    dC = (K2*C3(i-1)-K1*C1(i-1)*C2(i-1))*dt;
    C1(i)=C1(i-1) + dC;
    C2(i)=C2(i-1) + dC;
    C3(i)=C3(i-1) - 2 * dC;
end

plot(t, C1, 'g', t, C2, 'b', t, C3, 'r');
legend('C1', 'C2', 'C3');