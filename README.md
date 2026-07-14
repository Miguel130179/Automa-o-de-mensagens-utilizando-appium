# Automacao-o-de-mensagens-utilizando-appium
Projeto de appium feito no mobile

motivo:
esse projeto foi feito apenas para me entreter e aprender um pouquinho de appium.

oque faz:
ele basicamente manda mensagens específicas para um número de whatsapp

como esse projeto foi feito no mobile eu tive que configurar essas variáveis de ambiente no termux :
export ANDROID_HOME=$PREFIX/share/android-sdk
export PATH=$PATH:$ANDROID_HOME/tools:$ANDROID_HOME/platform-tools

e baixar as android build tools:
pkg install android-tools -y


para funcionamento(pelo menos no mobile que foi onde fiz) é necessário:
acessar as opções de desenvolvedor =>ligar depuração wifi => conectar no termux o endereço de ip e porta que aperecer utilizando o comando adb connect =>apertar o botão de "parear o disposivo com um código de pareamneto"
 =>utilizar o comando adb pair no termux e colocar o endereço ip,porta e logo em seguida o código de pareamento =>caso queira que ele ligue o cll  pra enviar a mensagens, acesse as opções de desenvolvedores e ative o "stay awake" logo após isso conecte o cll em um carregador => rode o appium no terminal =>e por fim rode o código.


Utilização da IA:
foi utilizado Ia para a descoberta das variáveis de ambiente que precisavam ser configuradas,para o descobrir o webdriver await,para também descobrir os action builders e descoberta das android build tools.A inplementação foi feita por mim
