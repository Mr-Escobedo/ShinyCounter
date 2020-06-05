import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class ShinyCounter implements KeyListener
{
	private Counter c = null;
	private JLabel label = null;
	private JFrame frame = null;
	private JPanel panel = null;
	private JLabel picLabel = null;

	public ShinyCounter()
	{
		c = new Counter();
		c.read();

		frame = new JFrame();
		frame.addKeyListener(this);

		panel = new JPanel();
		label = new JLabel("Eggs Hatched: " + c.getCount());
		picLabel = new JLabel();
		picLabel.setIcon(new ImageIcon("shiny_scorbunny.png"));

		panel.setBorder(BorderFactory.createEmptyBorder(300,300,100,300));
		panel.setLayout(new GridLayout(0, 1));
		panel.add(picLabel);
		panel.add(label);

		frame.add(panel, BorderLayout.CENTER);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.setTitle("Shiny Counter");
		frame.pack();
		frame.setVisible(true);
	}

	public static void main(String[] args)
	{
		new ShinyCounter();
	}

	@Override
	public void keyReleased(KeyEvent k)
	{
		//System.out.println("Released");
	}

	@Override
	public void keyPressed(KeyEvent k)
	{
		int keyCode = k.getKeyCode();
		switch(keyCode)
		{
			case KeyEvent.VK_UP:
				c.up();
				break;
			case KeyEvent.VK_DOWN:
				c.down();
				break;
			case KeyEvent.VK_LEFT:
				c.down();
				break;
			case KeyEvent.VK_RIGHT:
				c.up();
				break;
			case KeyEvent.VK_SPACE:
				c.up();
				break;
			case KeyEvent.VK_ENTER:
				c.resetCount();
				break;
		}

		int count = c.getCount();

		label.setText("Eggs Hatched: " + count);
		if(count % 5 == 0)
		{
			try
			{
				c.save();
			}
			catch(Exception e)
			{}
		}
		
	}

	@Override
	public void keyTyped(KeyEvent k)
	{
		//System.out.println("Typed");
	}
}
