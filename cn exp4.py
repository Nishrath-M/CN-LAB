Server.java
import java.io.*;
import java.net.*;
import java.util.*;
class Server
{
public static void main(String args[])
{
try
{
DatagramSocket server=new DatagramSocket(1309);
while(true)
{
byte[] sendbyte=new byte[1024];
byte[] receivebyte=new byte[1024];
DatagramPacket receiver=new
DatagramPacket(receivebyte,receivebyte.length);
server.receive(receiver);String str=new String(receiver.getData());
String s=str.trim();
//System.out.println(s);
InetAddress addr=receiver.getAddress();
int port=receiver.getPort();
String ip[]={"165.165.80.80","165.165.79.1"};
String
name[]={"www.aptitudeguru.com","www.downloadcyclone.blogspot.com"};
for(int i=0;i<ip.length;i++)
{
  sendbyte=name[i].getBytes();
DatagramPacket sender=new
DatagramPacket(sendbyte,sendbyte.length,addr,port);
server.send(sender);
break;
}
else if(s.equals(name[i]))
{
sendbyte=ip[i].getBytes();
DatagramPacket sender=new
DatagramPacket(sendbyte,sendbyte.length,addr,port);
server.send(sender);
break; } }
break;
} }
catch(Exception e)
{
System.out.println(e); }
} }
Client.java
import java.io.*;
import java.net.*;
import java.util.*;
class Client{
public static void main(String args[])
{
try
{
DatagramSocket client=new DatagramSocket();
InetAddress addr=InetAddress.getByName("127.0.0.1")
  byte[] sendbyte=new byte[1024];
byte[] receivebyte=new byte[1024];
BufferedReader in=new BufferedReader(new
InputStreamReader(System.in));
System.out.println("Enter the SERVER/DOMAIN NAME:");
String str=in.readLine();
sendbyte=str.getBytes();
DatagramPacket sender=new
DatagramPacket(sendbyte,sendbyte.length,addr,1309);
client.send(sender);
DatagramPacket receiver=new
DatagramPacket(receivebyte,receivebyte.length);
client.receive(receiver);
String s=new String(receiver.getData());
System.out.println("IP address is: "+s.trim());
client.close();
}
catch(Exception e)
{
System.out.println(e);
}
}
}

  
if(s.equals(ip[i]))
{
