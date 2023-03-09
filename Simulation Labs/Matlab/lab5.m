clf
clearvars

G(1)=35000;
N = 50

for i=1:N-1
    G(i+1) = mod(G(i)*27+1000,10000)+30000
end

Y(1)=50000;
for k= 2:N
    I(k) = 2+0.1*Y(k-1);
    Y(k) = 45.45+2.27*(I(k)+G(k));
    T(k) = 0.2*Y(k);
    C(k) = 20+0.7*(Y(k)-T(k));
end
plot(Y)
hold on
plot(C)
hold on
plot(I)
hold on
plot(T)
hold on
plot(G)
h = legend('National Income(Y)','Consumption(C)','Investment(I)','Taxes(T)','Expenditure(G)');