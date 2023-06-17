import java.io.*;
import java.net.*;

public class Server {
    public static void main(String[] args) throws Exception{
        // 1. Server starts listening (UDP/TCP)
        ServerSocket serverSocket = new ServerSocket(9876);
        System.out.println("TCP server started on port " + serverSocket.getLocalPort());

        // 2. Client makes a connection
        Socket connectionSocket = serverSocket.accept();
        System.out.println("Client is connected: " + serverSocket.getLocalPort());

        // 3. Wait for client to send the request
BufferedReader inFromClient = new BufferedReader(new InputStreamReader(connectionSocket.getInputStream()));
String clientCommand;
clientCommand = inFromClient.readLine();

    if(clientCommand.equals("play")){
        // 4. Read the file and send to client
        byte[] buffer = new byte[1024];
        FileInputStream fileStream = new FileInputStream("never_gonna_give_you_up.mp3");
        int bytesRead;

        while((bytesRead = fileStream.read(buffer,0,buffer.length))>0)
        {
            OutputStream outToClient = connectionSocket.getOutputStream();
            outToClient.write(buffer, 0, bytesRead);
            System.out.println("Sent " + bytesRead + " bytes to client.");
        }

        // 5. Finish file transfer
        System.out.print("Finish Music sent");
    }
    else{
        // 6. Send error message to client and ask for a new request

        DataOutputStream outToClient = new DataOutputStream(connectionSocket.getOutputStream());
        outToClient.writeBytes("Error Command\n");
        System.out.println("Wrong command!");
    }
        // 7. Close the connection
        connectionSocket.close();
        serverSocket.close();
    }
}