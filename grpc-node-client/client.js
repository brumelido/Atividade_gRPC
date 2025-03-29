const grpc = require('@grpc/grpc-js');
const protoLoader = require('@grpc/proto-loader');

// Carrega o arquivo .proto
const packageDefinition = protoLoader.loadSync('calculator.proto', {
    keepCase: true,
    longs: String,
    enums: String,
    defaults: true,
    oneofs: true
});
const calculatorProto = grpc.loadPackageDefinition(packageDefinition).calculator;

// Conecta ao servidor Python
const client = new calculatorProto.Calculator('localhost:50051', grpc.credentials.createInsecure());

// Faz uma requisição de soma
client.Sum({ a: 7, b: 5 }, (error, response) => {
    if (error) {
        console.error('Erro:', error);
    } else {
        console.log(`Resposta do servidor: ${response.result}`);
    }
});
