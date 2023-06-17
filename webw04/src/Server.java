import java.io.*;
import java.net.*;

public class Server {
    public static void main(String[] args) throws IOException {
        ServerSocket serverSocket = new ServerSocket(1234);
        System.out.println("Server started on port 1234");
        while (true) {
            Socket clientSocket = serverSocket.accept();
            System.out.println("Client connected: " + clientSocket.getInetAddress());
            ClientHandler clientHandler = new ClientHandler(clientSocket);
            clientHandler.start();
        }
    }
}

class ClientHandler extends Thread {
    private Socket clientSocket;
    private BufferedReader in;
    private PrintWriter out;

    public ClientHandler(Socket socket) throws IOException {
        clientSocket = socket;
        in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
        out = new PrintWriter(clientSocket.getOutputStream(), true);
    }

    public void run() {
        try {
            while (true) {
                String inputLine = in.readLine();
                if (inputLine == null) break;
                System.out.println("Received from client: " + inputLine);
                out.println("Server received: " + inputLine);
            }
            clientSocket.close();
        } catch (IOException e) {
            System.err.println("Error handling client: " + e);
        }
    }
}