package ;

import src.Infix;
import massive.munit.util.Timer;
import massive.munit.Assert;
import massive.munit.async.AsyncFactory;


class InfixTest 
{
	
	
	public function new() 
	{
		
	}
	
	@BeforeClass
	public function beforeClass()
	{
	}
	
	@AfterClass
	public function afterClass()
	{
	}
	
	@Before
	public function setup()
	{
	}
	
	@After
	public function tearDown()
	{
	}
	
	@Test 
	public function testPrefixToInfix0(){
		var infix:Infix = new src.Infix();
		var str = "+ - 13 4 55";
		Assert.areEqual("13-4+55", infix.start(str));
	}

	@Test 
	public function testPrefixToInfix1(){
		var infix:Infix = new src.Infix();
		var str = "+ 2 * 2 - 2 1";
		Assert.areEqual("2+2*(2-1)", infix.start(str));
	}

	@Test 
	public function testPrefixToInfix2(){
		var infix:Infix = new src.Infix();
		var str = "+ + 10 20 30";
		Assert.areEqual("10+20+30", infix.start(str));
	}

	@Test 
	public function testPrefixToInfix3(){
		var infix:Infix = new src.Infix();
		var str = "- - 1 2";
		Assert.areEqual("-(1-2)", infix.start(str));
	}

	@Test 
		public function testPrefixToInfix4(){
			var infix:Infix = new src.Infix();
			var str = "/ + 3 10 * + 2 3 - 3 5";
			Assert.areEqual("(3+10)/((2+3)*(3-5))", infix.start(str));
		}

	@Test 
		public function testPrefixToInfix5(){
			var infix:Infix = new src.Infix();
			var str = "/ - 3 10 * + 2 3 + 3 5 ";
			Assert.areEqual("(3-10)/((2+3)*(3+5))", infix.start(str));
		}

	@Test 
		public function testPrefixToInfix6(){
			var infix:Infix = new Infix();
			var str = "* 3 * 3 5 ";
			Assert.areEqual("3*3*5", infix.start(str));
		}

	
}