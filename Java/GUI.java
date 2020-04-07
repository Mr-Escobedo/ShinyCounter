import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

class GUI
{
	static Counter count;
	public static void main(String[] args)
	{
		ImageIcon target_image = new ImageIcon("../Resources/shiny_charmander.gif");
		count = new Counter(0, 1, "shiny_charmander.cnt");
		JFrame window = new JFrame("Pokémon Shiny Counter");
		JLabel target = new JLabel();
		JLabel display = new JLabel();
		JLabel odds = new JLabel("Odds: 1/512");
		odds.setFont(new Font("Serif", Font.PLAIN, 30));
		display.setFont(new Font("Serif", Font.PLAIN, 30));
		display.setText("Eggs Hatched: " + count.get_count());
		target.setIcon(target_image);

		display.setBounds(85, 160, 300, 200);
		odds.setBounds(100, 190, 200, 200);
		target.setBounds(75, 25, 200, 200);
		window.add(target);
		window.add(display);
		window.add(odds);
		window.setSize(400,400);
		window.setLayout(null);
		window.setVisible(true);
		window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}
}
