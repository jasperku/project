import java.io.*;
import java.net.*;
import java.util.Scanner;
import javazoom.jl.player.Player;

public class client {
    public static void main(String[] args) throws Exception{

        // 1. Connect server
        Socket clientSocket = new Socket("localhost", 9876);
        System.out.println("Connected to server.");

        // 2. Send command request
        DataOutputStream outToServer = new DataOutputStream(clientSocket.getOutputStream());
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a command (play):");
        String request = scanner.nextLine();
        outToServer.writeBytes(request+ '\n');
        //System.out.println("Request sent to server:" + request);

        // 3. Get the mp3 file from server or error message
        InputStream inFromServer = clientSocket.getInputStream();
        FileOutputStream fileStream = new FileOutputStream("received_music.mp3");
        byte[] buffer = new byte[1024];
        int bytesRead;

        // read the response from server
        DataInputStream dataInFromServer = new DataInputStream(inFromServer);
        String response = dataInFromServer.readLine();

        if (response.equals("Error Command")) {
            System.out.println(response);
        } 
        else {
            // read the file from server
            while ((bytesRead = inFromServer.read(buffer, 0, buffer.length)) > 0) {
                fileStream.write(buffer, 0, bytesRead);
                System.out.println("Received " + bytesRead + " bytes from server.");
            }
            fileStream.close();
            inFromServer.close();
            System.out.println("Music received");
            // 4. Play the mp3 file if the command is "play"
            if (request.equals("play")) {
                System.out.println("Playing music");
                FileInputStream fis = new FileInputStream("received_music.mp3");
                Player player = new Player(fis);
                player.play();
            }
        }
// 5. Close the connection
        clientSocket.close();
    }
}