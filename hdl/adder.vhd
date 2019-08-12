-- Adder DUT
library ieee ;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity adder is
generic(
    DATA_WIDTH : positive := 4);
port(
  clk : in  std_logic;
  A   : in  std_logic_vector(DATA_WIDTH-1 downto 0);
  B   : in  std_logic_vector(DATA_WIDTH-1 downto 0);
  X   : out std_logic_vector(DATA_WIDTH-1 downto 0)
);
end adder;

architecture RTL of adder is
  signal test : std_logic;
begin

  process(clk) begin
    test <= A(0);
    X <= std_logic_vector(unsigned(A)+unsigned(B));
  end process;

end RTL;
