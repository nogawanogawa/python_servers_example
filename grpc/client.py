import grpc
from pb import cosine_similarity_pb2
from pb import cosine_similarity_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:5001') as channel:
        stub = cosine_similarity_pb2_grpc.CosineSimServiceStub(channel)
        response = stub.calc_cosine_sim(
            cosine_similarity_pb2.CosineSimRequest(
                v1="001", v2="102"
            )
        )
    print("Response: %s" % response.cosinesim)


if __name__ == '__main__':
    run()
