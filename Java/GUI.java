import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class GUI implements ActionListener
{
	int count = 0;
	JLabel label = null;
	public GUI()
	{
		JFrame frame = new JFrame();
		JButton button = new JButton("Click Me");
		button.addActionListener(this);
		JPanel panel = new JPanel();
		label = new JLabel("Number of Clicks: 0");

		panel.setBorder(BorderFactory.createEmptyBorder(30,30,10,30));
		panel.setLayout(new GridLayout(0, 1));
		panel.add(button);
		panel.add(label);

		frame.add(panel, BorderLayout.CENTER);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.setTitle("GUI Tutorial");
		frame.pack();
		frame.setVisible(true);
	}

	public static void main(String[] args)
	{
		new GUI();
	}

	@Override
	public void actionPerformed(ActionEvent e)
	{
		count++;
		label.setText("Number of Clicks: " + count);
	}
}
