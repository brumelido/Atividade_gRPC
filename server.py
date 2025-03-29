import grpc
from concurrent import futures
import time

import calculator_pb2
import calculator_pb2_grpc

# Implementação do serviço Calculator
class CalculatorServicer(calculator_pb2_grpc.CalculatorServicer):
    def Sum(self, request, context):
        # Soma os valores recebidos na requisição
        result = request.a + request.b
        print(f"Recebido: {request.a} + {request.b} = {result}")
        return calculator_pb2.SumResponse(result=result)

def serve():
    # Cria um servidor gRPC com um pool de 10 threads
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_pb2_grpc.add_CalculatorServicer_to_server(CalculatorServicer(), server)
    
    # Define a porta para escutar as requisições
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Servidor gRPC iniciado na porta 50051.")
    
    try:
        while True:
            time.sleep(86400)  # mantém o servidor ativo por 1 dia
    except KeyboardInterrupt:
        server.stop(0)
        print("Servidor interrompido.")

if __name__ == '__main__':
    serve()
