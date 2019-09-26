module basic_and_tb();

  reg [3:0] a, b;
  wire [3:0] out;

  basic_and #(.WIDTH(4)) DUT (
    .a(a),
    .b(b),
    .out(out)
  );

  initial begin
    $dumpfile("test.vcd");
    $dumpvars(0,basic_and_tb);

    a = 4'b0000;
    b = 4'b0000;
    #20
    a = 4'b1111;
    b = 4'b0101;
    #20
    a = 4'b1100;
    b = 4'b1111;
    #20
    a = 4'b1100;
    b = 4'b0011;
    #20
    a = 4'b1100;
    b = 4'b1010;
    #20
    $finish;
  end

endmodule
