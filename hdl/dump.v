module dump;
    initial begin
        $dumpfile("test.vcd");
        $dumpvars(0,basic_and_tb);
        #5 $finish;
    end
endmodule
