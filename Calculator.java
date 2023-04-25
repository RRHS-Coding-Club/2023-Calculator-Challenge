import java.awt.Color;
import java.awt.Dimension;
import java.awt.Font;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JTextField;

public class Calculator extends JPanel implements ActionListener {
	//class variables
	final int WIDTH = 300;
	final int HEIGHT = 400;
	
	//instance variables
	JTextField jtWindow;
	Font font = new Font("Papyrus", Font.PLAIN, 18);
	
	//button variables
	JButton b0, b1, b2, b3, b4, b5, b6, b7, b8, b9;
	JButton bEqual, bAdd, bSub, bMult, bDiv, bDec, bClear, bMod, bSquare, bNeg;
	
	//value holders
	double firstNum, secondNum, result;
	String operation = "", answer;
	
	//constructor
	public Calculator()
	{
		this.setPreferredSize(new Dimension(WIDTH, HEIGHT));
		this.setBackground(Color.DARK_GRAY);
		
		jtWindow = new JTextField(15);
		jtWindow.setFont(font);
		jtWindow.setHorizontalAlignment(JTextField.RIGHT);
		jtWindow.setEditable(false);
		
		this.add(jtWindow);
		
		//button panel
		JPanel buttonPanel = buildButtonPanel();
		this.add(buttonPanel);
	}
	private JPanel buildButtonPanel()
	{
		JPanel p = new JPanel();
		p.setLayout(new GridLayout(5, 4));
		p.setPreferredSize(new Dimension(WIDTH-10, HEIGHT-40));
		
		//build buttons
		//row 1 ******************************************************************
		b7 = new JButton("7");
		b7.setFont(font);
		b7.addActionListener(this);
		p.add(b7);
		
		b8 = new JButton("8");
		b8.setFont(font);
		b8.addActionListener(this);
		p.add(b8);
		
		b9 = new JButton("9");
		b9.setFont(font);
		b9.addActionListener(this);
		p.add(b9);
		
		bDiv = new JButton("÷");
		bDiv.setFont(font);
		bDiv.addActionListener(this);
		p.add(bDiv);
		//row 2 ******************************************************************
		b4 = new JButton("4");
		b4.setFont(font);
		b4.addActionListener(this);
		p.add(b4);
		
		b5 = new JButton("5");
		b5.setFont(font);
		b5.addActionListener(this);
		p.add(b5);
		
		b6 = new JButton("6");
		b6.setFont(font);
		b6.addActionListener(this);
		p.add(b6);
		
		bMult = new JButton("×");
		bMult.setFont(font);
		bMult.addActionListener(this);
		p.add(bMult);
		//row 3 ******************************************************************
		b1 = new JButton("1");
		b1.setFont(font);
		b1.addActionListener(this);
		p.add(b1);
		
		b2 = new JButton("2");
		b2.setFont(font);
		b2.addActionListener(this);
		p.add(b2);
		
		b3 = new JButton("3");
		b3.setFont(font);
		b3.addActionListener(this);
		p.add(b3);
		
		bSub = new JButton("-");
		bSub.setFont(font);
		bSub.addActionListener(this);
		p.add(bSub);
		//row 4 ******************************************************************
		bNeg = new JButton("±");
		bNeg.setFont(font);
		bNeg.addActionListener(this);
		p.add(bNeg);
		
		b0 = new JButton("0");
		b0.setFont(font);
		b0.addActionListener(this);
		p.add(b0);
		
		bDec = new JButton(".");
		bDec.setFont(font);
		bDec.addActionListener(this);
		p.add(bDec);
		
		bAdd = new JButton("+");
		bAdd.setFont(font);
		bAdd.addActionListener(this);
		p.add(bAdd);
		//row 5 ******************************************************************
		bClear = new JButton("C");
		bClear.setFont(font);
		bClear.addActionListener(this);
		p.add(bClear);
		
		bSquare = new JButton("x²");
		bSquare.setFont(font);
		bSquare.addActionListener(this);
		p.add(bSquare);
		
		bMod = new JButton("%");
		bMod.setFont(font);
		bMod.addActionListener(this);
		p.add(bMod);
		
		bEqual = new JButton("=");
		bEqual.setFont(font);
		bEqual.addActionListener(this);
		p.add(bEqual);
		//row end ****************************************************************
		
		
		return p;
	}
	@Override
	public void actionPerformed(ActionEvent e) {
		String command = e.getActionCommand(); // returns string on button
		
		if(command.charAt(0) == 'C')
		{
			jtWindow.setText("");
		}
		else if(command.charAt(0) == '+')
		{
			firstNum = Double.parseDouble(jtWindow.getText());
			jtWindow.setText("");
			operation = "+";
		}
		else if(command.charAt(0) == '-')
		{
			firstNum = Double.parseDouble(jtWindow.getText());
			jtWindow.setText("");
			operation = "-";
		}
		else if(command.charAt(0) == '×')
		{
			firstNum = Double.parseDouble(jtWindow.getText());
			jtWindow.setText("");
			operation = "×";
		}
		else if(command.charAt(0) == '÷')
		{
			firstNum = Double.parseDouble(jtWindow.getText());
			jtWindow.setText("");
			operation = "÷";
		}
		else if(command.charAt(0) == 'x')
		{
			jtWindow.setText("" + (Double.parseDouble(jtWindow.getText()) * Double.parseDouble(jtWindow.getText())));
		}
		else if(command.charAt(0) == '.')
		{
			if(!jtWindow.getText().contains("."))
			{
				jtWindow.setText(jtWindow.getText() + command);
			}
		}
		else if(command.charAt(0) == '%')
		{
			firstNum = Double.parseDouble(jtWindow.getText());
			jtWindow.setText("");
			operation = "%";
		}
		else if(command.charAt(0) == '±')
		{
			firstNum = Double.parseDouble(jtWindow.getText());
			jtWindow.setText("" + (-1 * (Double.parseDouble(jtWindow.getText()))));
		}
		//place your operations here
		else if(command.charAt(0) == '=')
		{
			if(!operation.equals(""))
			{
				secondNum = Double.parseDouble(jtWindow.getText());
				jtWindow.setText("");
				evaluate();
			}
		}
		else
		{
			jtWindow.setText(jtWindow.getText() + command);
		}
		
	}
	private void evaluate() {
		if(operation.equals(""))
		{
			result = firstNum;
		}
		else if(operation.equals("+"))
		{
			result = firstNum + secondNum;
		}
		else if(operation.equals("-"))
		{
			result = firstNum - secondNum;
		}
		else if(operation.equals("×"))
		{
			result = firstNum * secondNum;
		}
		else if(operation.equals("÷"))
		{
			if(secondNum == 0)
			{
				JOptionPane.showMessageDialog(this, "Error: Cannot divide by 0.");
				result = firstNum;
			}
			else
			{
				result = firstNum / secondNum;
			}
		}
		else if(operation.equals("%"))
		{
			result = firstNum % secondNum;
		}
		operation = ""; //Repeating operations does not work properly
		jtWindow.setText("" + result);
	}
}
