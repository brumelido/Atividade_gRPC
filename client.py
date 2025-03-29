import grpc
import calculator_pb2
import calculator_pb2_grpc

def run():
    # Conecta ao servidor na porta 50051
    channel = grpc.insecure_channel('localhost:50051')
    stub = calculator_pb2_grpc.CalculatorStub(channel)
    
    # Envia uma requisição de soma
    request = calculator_pb2.SumRequest(a=5, b=3)
    response = stub.Sum(request)
    
    print(f"Resposta do servidor: {response.result}")

if __name__ == '__main__':
    run()
