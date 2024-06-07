module adder #(
    parameter integer DATA_WIDTH = 4
) (
    input  logic unsigned [DATA_WIDTH - 1:0] a_i,
    input  logic unsigned [DATA_WIDTH - 1:0] b_i,
    input  logic carry_i,
    output logic unsigned [DATA_WIDTH - 1:0] sum_o,
    output logic carry_o
);

assign {carry_o, sum_o} = a_i + b_i + carry_i;

initial begin
    $dumpfile("dump.vcd");
    $dumpvars(1, adder);
end
    
endmodule